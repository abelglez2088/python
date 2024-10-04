import datetime
import hashlib
import usuarios.conexion as conexion

connect = conexion.ingresar()

database=connect[0]
cursor=connect[1]

print(database)
class Usuario:
    def __init__(self,nombre,apellidos,email,passw):
        self.nombre=nombre
        self.apellidos=apellidos
        self.email=email
        self.passw=passw
        
    def registrar(self):
        fecha=datetime.datetime.now()
               
        #cifrar contraseña
        
        cifrado=hashlib.sha256()
        cifrado.update(self.passw.encode('utf8'))    
        
        sql= """ 
        insert into usuario (nombre,apellidos,email,passw, fecha)  values(?,?,?,?,?)
        """
        usuario=(self.nombre,self.apellidos,self.email,cifrado.hexdigest(),fecha)
        try:
            
            cursor.execute(sql,usuario)
            database.commit()
            result = [cursor.rowcount,self]
        except:
            result=[0,self]
            
        return result

       
    def identificar(self):
        print("\nIngresatu email y contraseña...")
        #Consuslta para sasber si exite el usuario
        sql="""
        select * from usuario where email=? and passw=?
        """
      
        #cifrado de conytraseña
        cifrado=hashlib.sha256()
        cifrado.update(self.passw.encode('utf8'))  
     
        usuario=(self.email,cifrado.hexdigest())
        cursor.execute(sql,usuario)
        result= cursor.fetchone()
         
        print('contraseña: ',cifrado.hexdigest())  
        print('sql: ',sql, '   ', usuario )
        return result
        