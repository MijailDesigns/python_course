def holaMundo(nombre):
    return f"Hola que tal {nombre}"

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