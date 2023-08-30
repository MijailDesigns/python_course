video_games = {
    "accion": ["GTA", "COD", "PUGB"],
    "aventura": ["ASSINS", "CRASH", "Prince of persia"],
    "deportes": ["FIFA 21", "PRO 21", "MOTO GP 21"]
}

# for game in video_games:
#     print(game, video_games[game])

tabla = [
    {
        "categoria": "ACCION",
        "juegos": ["GTA", "COD", "PUGB"]
    },
    {
        "categoria": "AVENTURA",
        "juegos": ["ASSINS", "CRASH", "Prince of persia"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA 21", "PRO 21", "MOTO GP 21"]
    }
]

for item in tabla:
    result = ""
    for i in item['juegos']:
        #print(i)
        result = result + i + " "
    result2 = f"Los juegos de la categoria {item['categoria']} son {result}"
    #print(item["categoria"])
    print(result2)