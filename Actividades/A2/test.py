from io import StringIO
from unittest.mock import patch
import unittest

from test_corredor import VerificarCorredor
from test_carrera import VerificarCarrera


if __name__ == '__main__':
    with patch('sys.stdout', new=StringIO()):
        unittest.main(verbosity=2)
    # unittest.main()