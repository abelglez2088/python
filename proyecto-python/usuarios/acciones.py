import usuarios.usuario as modelo
import notas.acciones


class Acciones:

    def registro(self):
        print ("\nRegistro de usuario en el sistema")
        nombre=input("Registre su nombre: ")
        apellidos=input("Ingresa tus apellidos: ")
        email=input("Ingresa tu correo electronico: ")
        passw=input("Ingresa tu contraseña a 8 digitos: ")
        
        usuario = modelo.Usuario(nombre,apellidos,email,passw)
        registro = usuario.registrar()
        print(registro)
        
        if registro[0]>=1:
            print(f"\n {registro[1].nombre} te has registrado correctamente")
        else:
            print("\nHubo un error en el registro!!")
     
        
    def login(self):
        
        try:
            print("ingresa el usuario...")
            email=input("Ingresa tu correo electronico...")
            passw=input("Ingresa tu contraseña...")
            usuario=modelo.Usuario('','',email,passw)
            login = usuario.identificar()
            
            print(login)
            if email==login[3]:
                print(f"Bienvenido {login[1]}, te has regsitrados el {login[5]} ")
                self.proximasAcciones(login)
        except Exception as e:
          
            print(f"login incorrecto!! intenta de nuevo{e}")
            
        
    def proximasAcciones(self, usuario):
        
        modeloNotas=notas.acciones.Acciones()
        print("""
              Acciones Disponibles:
                1-Crear nota(crear)
                2-Mostrrar notas
                3-Eliminar notas
                4-Salir
              """)
        accion= input("\nlija una opcion...")
        
        if accion=="1":
            modeloNotas.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion=="2":
            modeloNotas.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion=="3":
            modeloNotas.Eliminar(usuario)
            self.proximasAcciones(usuario)
        elif accion=="4":
            exit()
        

        