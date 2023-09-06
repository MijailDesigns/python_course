#Programacion orientada a objetos

# Defiir un clase
class Coche:
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
    
micoche = Coche()
print(micoche.marca, micoche.color)
print(micoche.velocidad)
micoche.acelerar()
micoche.acelerar()
print(micoche.velocidad)
micoche.frenar()
print(micoche.velocidad)