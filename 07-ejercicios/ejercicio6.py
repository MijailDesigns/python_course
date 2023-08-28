tabla = int(input("Introducir el numero de la tabla que deseas: "))

if tabla < 1:
    print("El numero debe ser igual o mayor a 1")
else:
    print(f"Tabla del {tabla}")

    for contador in range(1,11):
        print(f"{tabla} x {contador} = {tabla*contador}")

    print(f"Fin tabla {tabla}")