import random
opciones = ["piedra","papel","tijera"]

def jugar():
    while True:
        jugador = input("Elige piedra, papel ó tijera ('salir para terminar')").lower()
        if jugador == "salir":
            print("fin del juego!!!!")
            break
        if jugador not in opciones:
            print("opcion inválida. intente de nuevo!!!.")
            continue
        computadora = random.choice(opciones)
        print (f"la comoputadora eligio {computadora}")
        if jugador == computadora:
            print("Es un empate!!!!")
        elif(jugador == "piedra" and computadora == "tijera")or\
            (jugador == "papel" and computadora == "piedra")or\
            (jugador == "tijera" and computadora == "papel"):
                print("has ganado!!! :)")
        else:
            print("has Perdido!!! :(")

jugar()   
             