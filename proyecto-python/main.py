"""
proyecto python mysql
-abrir asistente
-login o respeto
-si elegimos registro, creara un usuario en la BD
-si elegimos login, identifica al usuario y nos preguntará
-crear nota, mostrar notas, borrarlas
"""
from usuarios import acciones

print(""" 
    Acciones disponibles:
        1.-Registro
        2.-Login
      """)
opcion=acciones.Acciones()
accion = input("Que quieres hacer:? ")

if accion=="1":
   opcion.registro()
elif accion=="2":
   opcion.login()
else :
    print("Opcion no reconocida")
    
