import mysql.connector
import pyodbc

def conectar():
    
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="master_python"
    )
    cursor = database.cursor(buffered=True)
    return (database,cursor)

def ingresar():
    server = 'proserver'  # Cambia esto por el nombre de tu servidor SQL Server
    database = 'master_python'  # Cambia esto por el nombre de tu base de datos
    username = 'abgonzalez'  # Cambia esto por tu nombre de usuario
    password = 'E053672ab.'  # Cambia esto por tu contraseña
    driver = '{ODBC Driver 17 for SQL Server}'  # El nombre del controlador puede variar
    # Cadena de conexión
    connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    connection = None
    connection = pyodbc.connect(connection_string)
    #Creacion de uan tabla 
    cursor = connection.cursor()
    return(connection,cursor)