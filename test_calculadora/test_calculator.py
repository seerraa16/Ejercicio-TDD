import unittest
import math
from calculadora.calculator import calculadora

class TestCalculator(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        self.calc = calculadora()
    
    def test_suma(self):
        self.calc.suma(2, 2)
        self.assertEqual(self.calc.value, 4)
    
    def test_resta(self):
        self.calc.resta(4, 2)
        self.assertEqual(self.calc.value, 2)
    
    def test_multiplicar(self):
        self.calc.multiplicar(2, 2)
        self.assertEqual(self.calc.value, 4)
    
    def test_dividir(self):
        self.calc.dividir(4, 2)
        self.assertEqual(self.calc.value, 2)
    
    def test_potencia(self):
        self.calc.potencia(2, 2)
        self.assertEqual(self.calc.value, 4)
    
    def test_raiz(self):
        self.calc.raiz(4)
        self.assertEqual(self.calc.value, 2)
    
    def test_factorial(self):
        self.calc.factorial(4)
        self.assertEqual(self.calc.value, 24)
