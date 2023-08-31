import os, shutil

#Crear carpeta

if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("ya existe el directorio")

#Eliminar carpeta

#os.rmdir("./mi_carpeta")

#Copiar carpeta

# ruta_original = "./mi_carpeta"
# ruta_nueva = "./mi_carpeta_COPIADA"

# shutil.copytree(ruta_original, ruta_nueva)

#os.rmdir("./mi_carpeta_COPIADA")

#Lista archivos

print("Contenido de mi carpeta")
contenido = os.listdir("./mi_carpeta")
print(contenido)

for i in contenido:
    print(i)
