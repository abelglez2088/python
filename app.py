
import pyodbc
import pandas as pd



# Configura la conexión a la base de datos SQL Server
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=PROSERVER;"
    "DATABASE=SIGMAVI;"
    "UID=abgonzalez;"
    "PWD=E053672ab.;"
)
conn = pyodbc.connect(conn_str)

# Define la consulta SQL
query = "SELECT * FROM ACXCCAgenteTopeCta"

#
# Ejecuta la consulta y carga los datos en un DataFrame de pandas
df = pd.read_sql(query, conn)

# Guarda los datos en un archivo CSV en la misma carpeta
nombre_archivo = "resultados.csv"
df.to_csv(nombre_archivo, index=False)

print(f"Resultados guardados en {nombre_archivo}")