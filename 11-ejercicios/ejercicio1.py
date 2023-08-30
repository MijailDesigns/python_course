numeros = [8,2,1,6,4,7,3]
def recorrerLista(lista):
    result = ''
    for elem in lista:
        result = result + str(elem) +', '
    return result

print(recorrerLista(numeros))
numeros.sort()
print(numeros)
print(len(numeros))

numero_to_search = int(input("INtroduce el numero a buscar: "))
print(f"El numero {numero_to_search} se encuentra en el indice {numeros.index(numero_to_search)}")