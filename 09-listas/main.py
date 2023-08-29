peliculas = ["Batman", "Spiderman", "Señor de los anillos"]
cantantes = list(("JLO", "2pac", "Nina"))
years = list(range(2020, 2050))
variada = ["Pedro", 2, True]

# print(peliculas)
# print(peliculas[0])
# print(cantantes)
# print(years)
# print(variada)

#Indices

print(peliculas[0])
print(peliculas[-1])
print(cantantes[1:3])
print(cantantes[0:1])
print(peliculas[1:])
peliculas[0] = "Gran Torino"
print(peliculas)

#Añadir elementos a la lista

cantantes.append("Cantinflas")
cantantes.append("Ruben Blades")
print(cantantes)

#Recorrer listas

nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introducir nombre de pelicula: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)


for pelicula in peliculas:
    print(f"{peliculas.index(pelicula) + 1}. {pelicula}")

#Listas multidimensionales
