from wsgiref.simple_server import make_server, WSGIRequestHandler
import threading
import json
import copy
from urllib.parse import parse_qs
from datetime import date

# CONSTANTES
OK = "200 "
BAD = "400 "
NOT_FOUND = "404 "


class NoLoggingWSGIRequestHandler(WSGIRequestHandler):

    def log_message(self, format, *args):
        pass


class Server(threading.Thread):
    def __init__(self, host, port, database, mode=1) -> None:
        super().__init__()
        self.database = database
        self.host = host
        self.port = port
        self.mode = mode
        self.daemon = True

    def get(self, endpoint, params):
        if endpoint == "/":
            return self.get_index()
        elif endpoint in ["/horoscopo", "/horoscopo/"]:
            return self.get_horospoco(params)
        elif endpoint in ["/signos", "/signos/"]:
            return self.get_signos()
        elif endpoint in ["/aleatorio", "/aleatorio/"]:
            return self.get_signo_aleatorio()

        response = {"result": "Endpoint no existe"}
        return response, NOT_FOUND

    def get_index(self):
        today = str(date.today())
        if self.mode == 1:
            response = {
                "result": f"Hoy es {today} y es un hermoso día para recibir un horoscopo"}
        else:
            response = {
                "result": f"Hoy es {today} y me da gusto escribir horoscopos"}

        return response, OK

    def get_horospoco(self, params):
        response = {"result": ""}
        if "signo" not in params:
            response["result"] = "Falta información en la consulta"
            return response, BAD

        signo = params["signo"][0]
        response["signo"] = signo
        if signo not in self.database:
            response["result"] = "El signo no existe"
            return response, BAD

        response["result"] = self.database[signo]
        return response, OK

    def get_signo_aleatorio(self):
        if self.mode == 3:
            return {"result": "ups, no pude"}, "500 "
        index = 0 if self.mode == 1 else -1
        signo = list(self.database.keys())[index]
        response = {
            "result": f"http://{self.host}:{self.port}/horoscopo?signo={signo}"}
        return response, OK

    def get_signos(self):
        response = {"result": list(self.database.keys())}
        return response, OK

    def post(self, endpoint, data):
        response = {"result": ""}
        if endpoint not in ["/update", "/update/"]:
            response["result"] = "Endpoint no existe"
            return response, NOT_FOUND

        if "signo" not in data or "mensaje" not in data:
            response["result"] = "Falta información en la consulta"
            return response, BAD

        mensaje = data["mensaje"][0]
        if len(mensaje) < 5:
            response["result"] = "El mensaje debe tener más de 4 caracteres"
            return response, BAD

        signo = data["signo"][0]

        if signo not in self.database:
            self.database[signo] = mensaje
            response["signos"] = list(self.database.keys())
            response["result"] = "Información agregada con éxito"
            return response, OK

        response["result"] = "El signo ya existe, no puedes modificarlo"
        return response, BAD

    def put(self, endpoint, data):
        response = {"result": ""}
        if endpoint not in ["/update", "/update/"]:
            response["result"] = "Endpoint no existe"
            return response, NOT_FOUND

        if "signo" not in data or "mensaje" not in data:
            response["result"] = "Falta información en la consulta"
            return response, BAD

        mensaje = data["mensaje"][0]
        if len(mensaje) < 5:
            response["result"] = "El mensaje debe tener más de 4 caracteres"
            return response, BAD

        signo = data["signo"][0]

        if signo not in self.database:
            response["result"] = "El signo no existe"
            return response, BAD

        self.database[signo] = mensaje
        response["result"] = "Información actualizada con éxito"
        return response, OK

    def delete(self, endpoint, data):
        response = {"result": ""}
        if endpoint not in ["/remove", "/remove/"]:
            response["result"] = "Endpoint no existe"
            return response, NOT_FOUND

        response = {"result": ""}
        if "signo" not in data:
            response["result"] = "Falta información en la consulta"
            return response, BAD

        signo = data["signo"][0]
        if signo not in self.database:
            response["result"] = "El signo no existe"
            return response, BAD

        del self.database[signo]
        response["result"] = "Información eliminada con éxito"
        response["signos"] = list(self.database.keys())
        return response, OK

    def check_autorization(self, environ):
        if 'HTTP_AUTHORIZATION' not in environ:
            return False

        key = 'pepaiic2233' if self.mode == 1 else 'morenoiic2233'
        if environ['HTTP_AUTHORIZATION'] != key:
            return False

        return True

    def application(self, environ, start_response):
        path = environ["PATH_INFO"]
        method = environ["REQUEST_METHOD"]
        try:
            request_body_size = int(environ.get("CONTENT_LENGTH", 0))
        except ValueError:
            request_body_size = 0

        request_body = environ["wsgi.input"].read(request_body_size)
        body = parse_qs(request_body.decode("utf-8"), encoding="utf-8")
        params = parse_qs(environ["QUERY_STRING"])
        new_body, new_params = {}, {}
        for key in body:
            new_body[key.lower()] = body[key]
        for key in params:
            new_params[key.lower()] = params[key]

        response = {"result": "Método no permitido"}
        status = "405 "

        if method == "GET":
            response, status = self.get(path, new_params)
        else:
            if self.check_autorization(environ):

                if method == "POST":
                    response, status = self.post(path, new_body)
                elif method == "DELETE":
                    response, status = self.delete(path, new_body)
                elif method == "PUT":
                    response, status = self.put(path, new_body)
            else:
                response = {"result": "No tienes autorización"}
                status = "401 "

        content_type = "application/json"

        # response headers
        response = json.dumps(response).encode()
        headers = [("Content-Type", content_type),
                   ("Content-Length", str(len(response)))]

        start_response(status, headers)
        return [response]

    def run(self):
        self.w_s = make_server(host=self.host, port=self.port,
                               app=self.application,
                               handler_class=NoLoggingWSGIRequestHandler)
        self.w_s.serve_forever()

    def stop(self):
        self.w_s.server_close()


if __name__ == "__main__":
    HOST = "localhost"
    PORT = 4444
    print("Escuchando.... http://{}:{}/".format(HOST, PORT))
    DATABASE = {
        "acuario": "Hoy será un hermoso día",
        "leo": "No salgas de casa.... te lo recomiendo",
    }
    thread = Server(HOST, PORT, DATABASE)
    thread.start()
    input("Presiona [ENTER] para cerrar el servidor\n")
