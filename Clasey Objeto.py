class Alumno:
        
    def inicializar (self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        
    def imprimir(self):
        print("nombre: ",self.nombre)
        print("nota: ", self.edad)
        
    def mostrar_estado(self):
        if(self.edad>=18):
            print("mayor de edad")
        else:
            print("menor de edad")
        

alumno1=Alumno()
alumno1.inicializar("abel gonzalez",35)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2=Alumno()
alumno2.inicializar("mony",17)
alumno2.imprimir()
alumno2.mostrar_estado()