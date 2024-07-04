# RACIONAL
import numpy 
from xmlrpc.server import CGIXMLRPCRequestHandler


class NumeroRacional:

    def __init__(self,numerador,denominador=1):
        
        if type(numerador) is int and type(denominador) is int:
            self.numerador = numerador
            self.denominador = denominador
        else:
            print('El numerador y el denominador deben ser enteros')
    
    def __str__(self):
        return f'{self.numerador} / {self.denominador}'
    
    def cociente(self):
        return self.numerador / self.denominador

    def esinfinito(self):
        if self.denominador ==0:
            return True
        return False
    
    # METODOS ESTATICOS
    @staticmethod
    def __mcd(a, b):
        resto = 0
        maximo = max(a, b)
        minimo = min(a, b)
        while minimo > 0:
            resto = minimo
            minimo = maximo % minimo
            maximo = resto 
        return maximo

    def simplificar(self):
        div = self.__mcd(self.numerador, self.denominador)
        self.numerador = int(self.numerador / div)
        self.denominador = int(self.denominador / div)

    @staticmethod
    def __imprimir(num,den):
        print(f'{num} / {den} = {round(num/den,2)}')

    
    @staticmethod
    def suma(p,q):
        num = p.numerador * q.denominador + q.numerador * p.denominador
        den = p.denominador * q.denominador 
        NumeroRacional.__imprimir(num,den)
    
    @staticmethod
    def resta(p,q):
        num = p.numerador * q.denominador - q.numerador * p.denominador
        den = p.denominador * q.denominador 
        NumeroRacional.__imprimir(num,den)
    
    @staticmethod
    def producto(p,q):
        num = p.numerador * q.numerador 
        den = p.denominador * q.denominador 
        NumeroRacional.__imprimir(num,den)

    @staticmethod
    def division(p,q):
        num = p.numerador * q.denominador
        den = p.denominador * q.numerador 
        NumeroRacional.__imprimir(num,den)

    # METODOS DE CLASE
    @classmethod
    def random(cls):
        import random
        num = random.randrange(-100,100)
        den = random.randrange(-100,100)
        while den ==0:
            den=random.randrange(-100,100)
        return cls(num,den)

    @classmethod
    def cero(cls):
        return cls(0)

    @classmethod
    def uno(cls):
        return cls(1)

    @classmethod
    def real2rac(cls,numreal):
        import math
        num=numreal
        den=1 
        # 5.4 --> Entera = 5 , Decimal= 0.4
        decimal, entero = math.modf(num)
        while decimal !=0:
            num*=10   # 5.4*10 = 54
            den*=10   # 1*10   = 10
            decimal,enteri= math.modf(num)
        num= int(num)
        den= int(den)
        return cls(num,den) 
        


number1 = NumeroRacional(3,6)
print(number1)
print(f'El cociente de {number1} es {number1.cociente()}')

number2= NumeroRacional(3)
print(number2)

print('Simplificar Numero')
number3= NumeroRacional(225,330)
print(number3)
number3.simplificar()
print(number3)

# Oprecaiones Aritmeticas
print('\n\nOperiones Matemaicas\n')
print('Suma:')
print(number1, '+',number3)
NumeroRacional.suma(number1,number3)
print('Resta')
print(number1, '-',number3)
NumeroRacional.resta(number1,number3)
print('Resta')
print(number1, '*',number3)
NumeroRacional.producto(number1,number3)
print('Division')
print(number1, '/',number3)
NumeroRacional.division(number1,number3)

print('-----------------------------------')
print('\n\nMetodos de Clase\n')

number4=NumeroRacional.random()
print(number4)
number5=NumeroRacional.cero()
print(number5)
number6= NumeroRacional.real2rac(5.4)
print(number6)
