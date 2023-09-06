#Programacion orientada a objetos

# Defiir un clase
class Coche:
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
    
micoche = Coche()
micoche.setColor("Gris")
micoche.setModelo("Murcielago")
print(micoche.marca, micoche.getModelo(), micoche.getColor())
print(micoche.getVelocidad())
micoche.acelerar()
micoche.acelerar()
print(micoche.velocidad)
micoche.frenar()
print(micoche.velocidad)