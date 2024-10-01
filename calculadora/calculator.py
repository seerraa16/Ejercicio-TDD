import math
class calculadora:
    def __init__(self):
        self.value = 0
    def suma(self, a, b):
        self.value = a + b

    def resta(self, a, b):
        self.value = a - b

    def multiplicar(self, a, b):
        self.value = a - b

    def dividir(self, a, b):
        self.value = a / b

    def potencia(self, a, b):
        self.value = a ** b

    def raiz(self, a):
        self.value = a ** 0.5
    
    def factorial(self, a):
        self.value = math.factorial(a)