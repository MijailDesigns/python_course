numero = int(input("Monto a calcular: "))
porcentaje = int(input("Porcentaje que deseas conocer: "))

result = numero * (porcentaje/100)
print(f"El {porcentaje}% de {numero} es {result}")