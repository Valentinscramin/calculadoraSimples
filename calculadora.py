import time 

class calculadora:
    def __init__(self, numberOne, numberTwo):
        self.numberOne = numberOne
        self.numberTwo = numberTwo

    def plusFunction (self):
        return self.numberOne + self.numberTwo

    def minusFunction (self):
        return self.numberOne - self.numberTwo

    def timesFunction (self):
         return self.numberOne * self.numberTwo

    def dividedFunction (self):
         return self.numberOne / self.numberTwo

    def powerFunction (self):
         return self.numberOne ** self.numberTwo

numero1 = int(input('Digite o numero 1: '))
print("\nOperadores:\n + \n - \n * \n / \n ^ \n")
operador = input('Digite o operador: ')
numero2 = int(input('Digite o numero 2: '))

calc = calculadora(numero1, numero2)

if operador == '+':
    result = calc.plusFunction()
elif operador == '-':
    result = calc.minusFunction()
elif operador == '*':
    result = calc.timesFunction()
elif operador == '/':
    result = calc.dividedFunction()
elif operador == '^':
    result = calc.powerFunction()

print("Resultado: "+str(result))
time.sleep(10)










