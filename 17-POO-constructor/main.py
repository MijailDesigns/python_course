from coche import Coche

carro = Coche("Azul", "Renault", "Clio", 120, 200, 4)
carro1 = Coche("Verde", "Seat", "Pnada", 240, 200, 4)
carro2 = Coche("Azul", "Citroen", "Xara", 100, 180, 4)
carro3 = Coche("Rojo", "Mercedez", "Clase A", 350, 400, 4)


print(carro.getColor())

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())