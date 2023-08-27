contador = 1
while contador <= 100:
    print(contador)
    contador += 1

contador = 1
resultado = str(0)
while contador <= 100:
    resultado = resultado + ", " + str(contador)
    contador += 1
print(resultado)


#tabla

tabla = int(input("Numero de la tabla: "))
contador = 0 
if tabla < 1:
    print("numero debe ser mayor a 1")
else:
    while contador <= 10:
        print(f"{tabla} x {contador} = {tabla*contador}")
        contador += 1
    print(f"fin tabla {tabla}")