tabla=[
    {
        "Categoria":"ACCION",
        "Juegos":["GTA,","CALL OF DUTY","PUGB"]
    },
    {
        "Categoria":"AVENTURA",
        "Juegos":["ASSASINS","CRASH BANDICOOT","PRINCE OF PERSIANS"]
    },
    {
        "Categoria":"DEPORTES",
        "Juegos":["FIFA","PES 21","MOTO GT"]
    },
    
]

for categoria in tabla:
    print (f"________{categoria['Categoria']}")
    for juego in categoria['Juegos']:
        print(juego)