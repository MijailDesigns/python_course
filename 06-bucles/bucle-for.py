
resultado = 0
for contador in range(1, 11):
    print(f"voy por el {str(contador)}")
    resultado += contador
print(resultado)

#Ejemplo tablas de multiplicar

tabla = int(input("¿Cual tabla de multiplicar deseas? "))
if tabla < 1:
    print("Numero debe ser mayor que 1")
else:
    for contador in range(11):
        print(f"{tabla} x {contador} = {tabla*contador}")
    print(f"fin tabla {tabla}")