from hdbcli import dbapi

def verificar_conexion():
    try:
        print("Estableciendo conexión con SAP HANA...")

        # Intentar establecer la conexión
        connection = dbapi.connect(
            address="vhmvods4db.sap.svrwes4h.com",
            port=30015,
            user="CUST_USER_ROLE_ADMIN",
            password="WRAq]v1J#kschyoeew486RhqzppNrN"
        )
        print("Conexión establecida exitosamente.")

        # Crear un cursor
        cursor = connection.cursor()
        print("Cursor creado exitosamente.")

        # Ejecutar una consulta de prueba
        cursor.execute("SELECT 'Conexión exitosa' FROM BUT020")
        print("Consulta ejecutada exitosamente.")

        # Obtener el resultado de la consulta
        resultado = cursor.fetchone()
        if resultado:
            print(f"Resultado de la consulta: {resultado[0]}")
        else:
            print("La consulta no devolvió ningún resultado.")

        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()
        print("Conexión cerrada exitosamente.")

    except dbapi.Error as e:
        # Manejar errores de conexión
        print(f"Error de conexión: {e}")

    except Exception as e:
        # Manejar otros errores
        print(f"Error inesperado: {e}")

# Llamar a la función para verificar la conexión
verificar_conexion()
