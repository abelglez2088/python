import pyodbc

# Parámetros de conexión
server = 'proserver'  # Cambia esto por el nombre de tu servidor SQL Server
database = 'IntelisisTmp'  # Cambia esto por el nombre de tu base de datos
username = 'abgonzalez'  # Cambia esto por tu nombre de usuario
password = 'E053672ab.'  # Cambia esto por tu contraseña
driver = '{ODBC Driver 17 for SQL Server}'  # El nombre del controlador puede variar

# Cadena de conexión
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
connection = None

connection = pyodbc.connect(connection_string)
#Creacion de uan tabla 

CursorInsertar = connection.cursor()
# El comando SQL para crear la tabla solo si no existe
sql_command = """
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[pruebaUDemy]') AND type = N'U')
BEGIN
    CREATE TABLE pruebaUDemy (
        id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
        titulo VARCHAR(100),
        Descripcion VARCHAR(100),
        precio FLOAT
    );
END
"""
CursorInsertar.execute(sql_command)

CursorInsertar = connection.cursor()
sql_commandInsertar="""
insert into pruebaUDemy values('curso de phyton','de novato a experto',10.45)
"""
CursorInsertar.execute(sql_commandInsertar)


CursorInsertar.execute("Select * from pruebaUDemy;")
cursos= CursorInsertar.fetchall()

for curso in cursos:
    print("ID: ", curso[0])
    print("Titulo: ", curso[1])
    print("Descripcion: ", curso[2])
    print("Precio: ", curso[3])
    print("\n")

##sirve para guardar los cambios 
connection.commit()


CursorInsertar.close()
connection.close()
