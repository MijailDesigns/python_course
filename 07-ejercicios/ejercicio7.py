numero1 = int(input("Introducir primer numero: "))
numero2 = int(input("Introducir segundo numero: "))

for contador in range(numero1, numero2 + 1):
    if contador % 2 != 0:
        print(f"{contador} es impar")