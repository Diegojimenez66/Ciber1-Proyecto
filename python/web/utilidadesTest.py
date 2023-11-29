import unittest
from utilidades import calculariva

class tests_calculariva(unittest.TestCase):
    def tests_mult021(self):
        self.assertEqual(calculariva(100), 21)

if __name__ == '__main__':
    unittest.main()