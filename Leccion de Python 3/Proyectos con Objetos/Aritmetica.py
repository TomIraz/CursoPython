class Aritmetica:

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):  # Metodo Suma
        return self.operandoA + self.operandoB

    def resta(self):  # Metodo Resta
        return self.operandoA - self.operandoB

    def multip(self):
        return self.operandoA * self.operandoB

    def division(self):
        return self.operandoA / self.operandoB


aritmetica1 = Aritmetica(6, 3)
print(f'Suma: {aritmetica1.sumar()}')
print(f'Resta: {aritmetica1.resta()}')
print(f'Multiplicacion: {aritmetica1.multip()}')
print(f'Division: {aritmetica1.division():.2f}')  # con :.1f indicas cuantos digitos flotantes queremos
