def suma(a, b):
    return a + b
# print(suma(4,5))

def muestraNombre():
    print("Mijail")

# muestraNombre()

def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es {nombre}")
    if edad > 18:
        print("Eres mayor de edad")
mostrarTuNombre("Mijail", 19)

def tabla(numero=3):
    print(f"Tabla de multiplicar del numero {numero}")
    for contador in range(11):
        print(f"{numero} x {contador} = {numero*contador}")
    

# tabla(5)
# tabla(7)
# tabla()

def calculadora(numero1, numero2, basicos= False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    div = numero1 / numero2

    cadena = ""

    if basicos: 
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion: " + str(multi)
        cadena += "\n"
        cadena += "Division: " + str(div)
    return cadena

# print(calculadora(5,5, True))

def getNombre(nombre):
    return f"El nombre es: {nombre}"

def getApellidos(apellidos):
    return f"Los apellidos son: {apellidos}"
print(getNombre("Mijail"))

def fullName(nombre, apellidos):
    return f"{getNombre(nombre)} \n {getApellidos(apellidos)}"
print(fullName("Mijail", "Pulgar"))

#Funcion lambda

dime_el_year = lambda year: f"El año es {year}"
print(dime_el_year(2022))