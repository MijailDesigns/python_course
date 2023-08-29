nombre = "Mijail"

comprobar = isinstance(nombre, str)
if comprobar:
    print("Es string")
else:
    print("No es una cadena")

if not isinstance(nombre, float):
    print("No es un decimal")

#Limpiar esapacios

frase = "   contenido "
print(frase)
print(frase.strip())

#eliminar variables
year = 2022
print(year)
del year
# print(year)

# Comporbar variable vacia

texto = " ff "
print(len(texto))

#encontrar caracteres

frase = "la vida"
print(frase.find("v"))
nueva_frase = frase.replace("vida", "familia")
print(nueva_frase)

#Mayusculas y minisculas
nombre = "Juan"
print(nombre.lower())
print(nombre.upper())