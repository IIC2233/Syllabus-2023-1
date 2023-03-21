# Descuentos :chart_with_downwards_trend:

Al momento de corregir una tarea, es posible que se apliquen penalizaciones sobre la nota final de esta en caso de encontrarse con ciertas faltas al formato estándar de `Python` o prácticas que dificulten la corrección al equipo docente.

Los descuentos finales aplicados sobre una tarea se calcularán de la siguiente forma:

#### <center>`mín(descuentos_miscelaneos, 10) + descuento_por_usar_algo_prohibido`</center>

Donde:
* [`descuentos_miscelaneos`](#Descuentos-Misceláneos) es la suma entre los descuento de PEP8, Readme, Modularización, Formato de entrega, Uso de `.gitignore` y descuentos adicionales. (Los demás descuentos que no son por atraso, ni uso de elementos prohibidos)
* [`descuento_por_usar_algo_prohibido`](#librerías-o-built-ins-prohibidos) es el descuento asociado a utilizar alguna librería o `Built-in` no autorizado.


***

## Descuentos Misceláneos

## PEP8 (hasta 4 décimas) :pencil2: 
PEP8 es el estándar que se utiliza para programar en `Python` :snake:, por lo que es importante que se sigan las convenciones. Todo tipo de detalle sobre estas convenciones se encuentran en la [guía de estilo](https://github.com/IIC2233/contenidos/blob/master/semana-00/1-gu%C3%ADa-de-estilo.ipynb).

De los cuales sólo se verificarán:
1. No exceder el máximo de **100** caracteres **por línea**.
2. Uso de variables declarativas y aclarativas.
3. Uso adecuado de CamelCase y snake_case.
4. Espacio después de la coma (",").
5. Uso de espacios para indentación y **no** de tabulaciones.
6. Uso de varuables globales. 
7. Utilizar correctamente los `import` (no hacer `import *`). Para más información de cómo importar archivos revisar [los contenido del curso](https://github.com/IIC2233/contenidos/blob/master/semana-00/2-modularizaci%C3%B3n.ipynb).

La cantidad de décimas a descontar será la siguiente (acorde a lo establecido arriba):
- **2 décimas** si no se cumple _sólo_ 1
- **3 décimas** si no se cumplen 2
- **4 décimas** si no se cumplen 3 _o más_

La búsqueda de estos tipos de errores tampoco debe ser una búsqueda exhaustiva, pero es altamente probable que los _linters_ se los muestren. Si sólo ven _un_ error de algún tipo siendo que en el resto de los casos no ocurre, entonces se puede perdonar.

## README (5 décimas) :page_facing_up: 

El _README.md_ es el archivo de texto escrito que se entrega junto a la tarea con el objetivo de explicar la tarea que realizaron y facilitar la corrección del ayudante. Se **recomienda fuertemente** ir completando este archivo a medida que se desarrolla la tarea. De este modo, se asegura la creación de un buen y completo _README.md_.

La cantidad de décimas a descontar se evalúa según los siguientes criterios:

- **1 décima** Si no se indica(n) los archivos principales que son necesarios para ejecutar la tarea o su ubicación dentro de su carpeta se hará este descuento.
- **Hasta 4 décimas** si el _README.md_ no incluye aspectos implementados y no implementados, o bien cualquier información relevante para la corrección.


## Modularización (5 décimas) :package: 

Se descuentan **5 décimas** si uno o más archivos exceden las **400** líneas de código.


## Formato de entrega (hasta 5 décimas) :inbox_tray: 
 1. Lenguaje vulgar (groserías) o inapropiado para el curso.
 2. Nombres o extensiones de archivos no explícitos ni declarativos.
 3. Utilizar _paths_ absolutos en una tarea en vez de _paths_ relativos. Para más información revisar [los contenidos del curso](https://github.com/IIC2233/contenidos/blob/master/semana-00/3-paths.ipynb).
 4. No respetar lo solicitado en el enunciado, o detallado en las issues.
 5. Utilizar código de internet sin citar. 
 
Dependiendo de la gravedad de no respetarlo, el descuento de cada ítem puede ir de 1 a 5 décimas.
Los descuentos de estos ítem son acumulables hasta un máximo de 5 décimas de descuento.

## Uso de `.gitignore` (hasta 5 décimas) :hand: 

El `.gitignore` es un archivo que permite indicar cuales archivos deben ser ignorados del repositorio, es decir, que no son detectados dentro de este al momento de querer hacer `git add`. Para más información visitar [este link](https://git-scm.com/docs/gitignore).

Este descuento sólo se aplica si en el enunciado de la tarea se especifica que **utilicen el `.gitignore`** o se indica que **no deben subir algún archivo en específico**. En caso de solicitar que usen el `.gitignore`, el descuento puede ser por uno de los 3 siguientes casos:
- **5 décimas** si no está el `.gitignore` y sube las cosas de todos modos.
- **2 decimas** si no está el gitignore pero no están subidas las cosas (no se puede evaluar el correcto uso de `.gitignore`)
- **2 décimas** si sube igual los archivos a ignorar a pesar de tener el archivo `.gitignore` (no cumple con el objetivo del `.gitignore` o no lo utiliza correctamente)
- **Importante:** el `.gitignore` debe estar dentro de la carpeta (T01/, T02/ o T03/), no se aceptará que lo pongan en otra parte aunque funcione.

## Cambio de líneas (hasta 5 décimas) :arrows_counterclockwise:
Por tarea, se permite cambiar **hasta** 20 líneas de código. Esta solicitud de cambio **solamente** se puede realizar mediante el mismo _README_ o bien en el **formulario de recorrección** de la tarea. Por cada línea del que cambien de su código se les aplicará un descuento según la siguiente fórmula:

### <center>`techo(c_lineas/4)`</center>

Donde `c_lineas` es la cantidad de líneas cambiadas.

***

## Librerías o Built-ins prohibidos

Junto a cada enunciado de tarea, se publicará una _issue_ con un listado de librerías cuyo uso está permitido para la tarea. En esa misma _issue_ también se incluirá un listado de librerías o _built-ins_ que se considerarán prohibidos y no podrán ser utilizados por el estudiante para la tarea.

El descuento por utilizar algo que se encuentre prohibido puede ir desde 1 décima a 5 décimas dependiendo del tipo de librería prohibida utilizada, además de la pérdida de puntaje en todos los _items_ de la rúbrica de corrección que se vean beneficiados por su uso.

Tal como dice en cada enunciado de tarea, no se permite ninguna librería a no ser que nosotros especifiquemos lo contrario, por lo que es responsabilidad del estudiante preguntar por el uso de cualquier librería que no se encuentre en ninguno de los listados de librerías prohibidas o permitidas.