import random
#variables
numero=-1
aleatorio=random.randint(0,100)

while numero !=aleatorio:
    numero=int(input("Ingresa el número del 0 al 100"))
    if numero==aleatorio:
        print("Has ganado!!! :)" )
    else:
        print("sigue intentando :(")
    print ("numero aleatorio",aleatorio)