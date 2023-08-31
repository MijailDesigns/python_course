from io import open
import pathlib

#Abrir un archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"

archivo = open(ruta, "a+")

#Escribir

archivo.write("Hola Mundo\n")

#Cerrar archivo

archivo.close()