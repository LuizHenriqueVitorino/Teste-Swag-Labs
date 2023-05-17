import sys
import os

# Adicione o caminho para o diretório raiz do seu projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from suites.testes_suite import TestesSuite



runner = unittest.TextTestRunner()
runner.run(TestesSuite().suite)