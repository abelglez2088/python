import psycopg2
from psycopg2 import Error

def llenar_control_integracion(id_anterior, id_nuevo):
    try:
        # Configurar la conexión a tu base de datos PostgreSQL
        with psycopg2.connect(
            host="172.16.202.75",
            database="AdminDoc",
            password="dbapostgres#$",
            user="postgres"
        ) as connection:
            with connection.cursor() as cursor:
                # Llamar al procedimiento almacenado
                cursor.callproc('spcontrol_integracion', (id_anterior, id_nuevo))

                # Opcional: Realizar commit de los cambios si es necesario
                # connection.commit()

                print("Procedimiento almacenado ejecutado correctamente.")

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error al ejecutar procedimiento almacenado: {error}")

# Llamada de ejemplo al procedimiento almacenado desde Python
llenar_control_integracion('I23rfre34234', 12345)
