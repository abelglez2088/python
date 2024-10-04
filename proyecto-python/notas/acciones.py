import notas.nota as modelo

class Acciones:
    
    def crear(self,usuario):
    
        
        print(f"\nCrear nueva nota...")
        titulo=input("Introduce el titulo de tu nota: ")
        descripcion=input("Introduce la descripcion: ")
        nota= modelo.Nota(usuario[0],titulo,descripcion)
        
        guardar = nota.guardar()
        
        if guardar[0]>=1:
            print(f"\nNota. {nota.titulo} guardado correctamente!")
        else:
            print(f"\nError al guardar nota")
    
    def mostrar(self,usuario):
        print(f"\nVale {usuario[1]} !! Notas: ")
        
        nota = modelo.Nota(usuario[0])
        notas = nota.Listar()
       
        for nota in notas:
            print("\n********************************")
            print(nota[2])
            print(nota[3])
    
    def Eliminar(self,usuario):
        print(f"\n Eeliminar...")
        titulo=input("Introduce el titulo de la nota: ")
        nota=modelo.Nota(usuario[0],titulo)
        delete=nota.Eliminar()
        if delete[0]>0:
            print(f"\n La nota {nota.titulo} ah sido eliminada")
        else:
            print(f"\nError al eliminar nota")