from io import open
import pathlib
import shutil

#Abrir un archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"

archivo = open(ruta, "a+")

#Escribir

archivo.write("Hola Mundo\n")

#Cerrar archivo

archivo.close()

#Abrir un archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"

archivo_lectura = open(ruta, "r")

#Leer contenido
# contenido = archivo_lectura.read()
# print(contenido)

#Leer contenido y guardarlo en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

for elem in lista:
    # lista_frase = elem.split()
    # print(lista_frase)
    # print("- "+elem.upper())
     print("- "+elem.center(50))

#Copiar archivos
# ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
# ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
# ruta_alternativa = str(pathlib.Path().absolute()) + "/../07-ejercicios/fichero_copiado88.txt"

# shutil.copyfile(ruta_original, ruta_nueva)

#Mover

ruta_original = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"

shutil.move(ruta_original, ruta_nueva)