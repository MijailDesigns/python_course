#Capturar excepciones y manejar errores en codigo 
#susceptible a fallos/errores

# try:
#     nombre = input("Cual es tu nombre?: ")
#     if len(nombre) > 1:
#         nombre_usuario = "Elnombre es " + nombre
#     print(nombre_usuario)
# except:
#     print("Ha ocurrido un error, mete bien el nombre")
# else:
#     print("Todo ha funcionado correctamente")
# finally:
#     print("Finalizado")

#Multiples excepciones

try:
    numero = int(input("dime el numero para elevarlo al cuadrado: "))
    print("El cuadrado es "+ str(numero*numero))
except TypeError:
    print("Debes convertir tus cadenas a enteros en el codigo")
except ValueError:
    print("Introduce un numero correcto")
except Exception as error:
    print(type(error))
    print(f"Ha ocurrido un error: {type(error).__name__}")