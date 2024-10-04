#atributos y propiedades

class Coche:
    color="rojo"
    marca="vw"
    modelo=2001
    velocidad=200
    caballosFuerza=500
    plazas=4
    
    def acelerar(self):
        self.velocidad+=1
        
    def frenar(self):
        self.velocidad -=1
        
    
    def getVelocidad(self):
        return self.velocidad
    
coche = Coche()

print(coche.velocidad)
coche.frenar()
print (coche.velocidad)