#Capturar excepciones y manejar errores en codigo 
#susceptible a fallos/errores

try:
    nombre = input("Cual es tu nombre?: ")
    if len(nombre) > 1:
        nombre_usuario = "Elnombre es " + nombre
    print(nombre_usuario)
except:
    print("Ha ocurrido un error, mete bien el nombre")
else:
    print("Todo ha funcionado correctamente")
finally:
    print("Finalizado")

