import usuarios.conexion as conexion
connect = conexion.ingresar()
database =connect[0]
cursor=connect[1]

class Nota:
    
    def __init__ (self, idUsuario,titulo="",descripcion=""):
        self.idUsuario=idUsuario
        self.titulo=titulo
        self.descripcion =descripcion
        
    def guardar(self):
     
        sql="insert into notas(idUsuario, titulo, descripcion, fecha) values (?,?,?,GETDATE())"
        nota =(self.idUsuario,self.titulo,self.descripcion)
        
        print(sql)
        print(nota)
        cursor.execute(sql,nota)
        database.commit()
            
        return [cursor.rowcount, self]
    
    def Listar(self):
        sql = f"select * from notas where idUsuario = {self.idUsuario}"
        cursor.execute(sql)
        result = cursor.fetchall()
        
        return result
    
    def Eliminar(self):
        sql=f"delete from notas where idusuario = {self.idUsuario} and  titulo= '{self.titulo}'"
        cursor.execute(sql)
        database.commit()
        
        return [cursor.rowcount,self] 