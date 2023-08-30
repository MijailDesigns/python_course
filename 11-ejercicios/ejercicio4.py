lista = ["hola", 1]
texto = "Hola"
entero = 1
boolean = True

def traducirTipo(tipo):
    tipos = {
        list: "LISTA",
        str: "STRING",
        bool: "BOOLEAN",
        int: "ENTERO"
    }
    return tipos[tipo]

def comprobarTipos(dato, tipo):
    test = isinstance(dato, tipo)
    result = ""
    if test: 
        result = f"Este dato es del tipo {traducirTipo(type(dato))}"
    else:
        result = None
    return result

print(comprobarTipos(texto, str))
print(comprobarTipos(lista, list))
print(comprobarTipos(entero, int))
print(comprobarTipos(boolean, bool))

