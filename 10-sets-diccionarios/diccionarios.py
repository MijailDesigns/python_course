persona = {
    "nombre": "Mijail",
    "apellido": "Pulgar",
    "web": "Mijail.com"
}

print(persona)
print(type(persona))
print(persona["apellido"])

#Lista con diccionarios

contactos = [
    {
        "nombre": "Mijail",
        "numero": 65456465,
    },
    {
        "nombre": "Luis",
        "numero": 5464564
    },
    {
        "nombre": "Salvador",
        "numero": 5465465
    }
]

contactos[1]["nombre"] = "javier"
print(contactos)
print(contactos[0]["nombre"])

for contacto in contactos:
    print(contacto["nombre"])
    print(contacto["numero"])
    print("--------------------")


