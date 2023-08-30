# import mimodulo
# from mimodulo import holaMundo
from mimodulo import *

print(holaMundo("Mijail"))
print(calculadora(3,5,True))

#modulo de fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)
print(fecha_completa.hour)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print(fecha_personalizada)

print(datetime.datetime.now().timestamp())
print(datetime.datetime.now().time())

#Modulo matematicas

import math

print("Raiz cuadrada de 10: ", math.sqrt(10))

print("Numero pi: ", float(math.pi))

print("Redondear: ", math.ceil(math.pi))

print("Redondear: ", math.floor(math.pi))

#Modulo random

import random

print("Numero aleatorio entre 15 y 67: ", random.randint(15, 67) )
