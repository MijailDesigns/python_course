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