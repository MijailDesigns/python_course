cantantes = ['2pac', 'Julio Iglesias', 'Ruben Blades']
numeros = [1,2,5,8,3,4]

#Order lista
print(numeros)
numeros.sort()
print(numeros)

#Añadir
cantantes.append('Sonora Ponceña')
cantantes.insert(1, 'Hector Lavoe')
print(cantantes)

#Eliminar elemento

cantantes.pop(0)
cantantes.remove('Julio Iglesias')
print(cantantes)

# Dar la vuelta

numeros.reverse()
print(numeros)

# Buscar dentro de una lista
print('Ruben Blades' in cantantes)

#Contar elemento
print(len(cantantes))

#Cuantas veces aparece un elementos
numeros.append(8)
print(numeros.count(8))

#Conseguir indice

print(cantantes.index('Ruben Blades'))

#Unir listas

cantantes.extend(numeros)
print(cantantes)