import sys
import os

# Adiciona o caminho para o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from suites.testes_suite import TestesSuite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(TestesSuite().suite)