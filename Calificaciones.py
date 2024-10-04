class Calificacion:
    
    def __init__(self):
        self.nombres=[]
        self.nota=[]
        
    def menu(self):
        opcion=0
        while opcion!=4:
            print("1.-Cargar Alumnos")
            print("2.-Listar Alumnos")
            print("3.-listado de alumnos con notas mayores o iguales a 7")
            print ("4.-Finalizar programas")
            opcion=int(input("ingrese una opcion: "))
            if opcion==1:
                self.Cargar()
            elif opcion==2:
                self.Listar()
            elif opcion==3:
                self.notas_altas()
                    
    def Cargar(self):
        for  x in range(5):
            nom=input("ingrese el nombre del alumno: ")
            self.nombres.append(nom) 
            no=int(input("nota del alumno: "))
            self.nota.append(no)
            
    def Listar(self):
        print("listado completo de alunmos: ")
        for x in range(5):
            print (self.nombres[x],self.nota[x])
            print("_______________")
            
    def notas_altas(self):
            print("Alumnos con notas superiores o iguales a 7")
            for x in range(5):
                if self.nota[x]>=7:
                    print(self.nombres[x],self.nota[x])
            print("_____________________") 

calif = Calificacion()   
calif.menu()