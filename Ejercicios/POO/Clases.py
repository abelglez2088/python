class Vehiculo():
    color=None
    longitud_metros=None
    ruedas=4
    
    #Métodos 
    def prender(self):
        print("El motor esta encendido")
    def acelerar(self):
        print("Ah acelerado")
    def detener(self):
        print("El vehiculo se ah detenido")
    def apagar(self):
        print("El vehiculo se ah apagado")    
    
    
objetoClase=Vehiculo()

objetoClase.prender()