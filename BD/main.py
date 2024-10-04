import mysql.connector
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)

cursor = database.cursor()
cursor.execute("""
create table if not exists vehiculos(
    idVehiculo int auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    constraint pk_vehiculo primary key(idVehiculo)
)
               
""")

#cursor.execute("insert into vehiculos values(null,'Volkswagen','vento 2017',120.500)")
coches=[
    ('Seat','Ibiza',1000000),
    ('Renault','clio',90000),
    ('Mercedez','cl500',530000),
    
]
cursor.executemany("insert into vehiculos values(null,%s,%s,%s)",coches)

database.commit()