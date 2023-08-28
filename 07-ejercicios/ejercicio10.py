
aprobados = 0
suspendidos = 0
contador = 1
cantidad = int(input("Introduce cantidad de alumnos a evaluar: "))

while contador <= cantidad:
    nota = int(input(f"Introduce nota de alumnos numero {contador}: "))
    if nota < 10:
        suspendidos += 1
    else:
        aprobados += 1
    contador += 1
print(f"Aprobados: {aprobados}, Suspendidos: {suspendidos}")