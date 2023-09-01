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

# try:
#     numero = int(input("dime el numero para elevarlo al cuadrado: "))
#     print("El cuadrado es "+ str(numero*numero))
# except TypeError:
#     print("Debes convertir tus cadenas a enteros en el codigo")
# except ValueError:
#     print("Introduce un numero correcto")
# except Exception as error:
#     print(type(error))
#     print(f"Ha ocurrido un error: {type(error).__name__}")

#Excepciones personalizadas o lanzar excepcion
try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no esta completo")
    else:
        print(f"Bienvenido al Master en Python {nombre}")
except ValueError:
    print("Introduce los datos correctamente")
except Exception as e:
    print(f"Existe un error: {e}")