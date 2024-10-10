# Inicialización de variables
prc = 0  # puntaje principal correcto
rc = 0   # respuesta correcta
pri = 0  # puntaje principal incorrecto
ri = 0   # respuesta incorrecta
prb = 0  # puntaje principal en blanco
rb = 0   # respuesta en blanco
pf = 0   # puntaje final

print("\n================================Ingresar Valores===========================")

# Entrada de puntajes
rc = int(input("Ingresa el puntaje de respuesta correcta: "))
ri = int(input("Ingresa el puntaje incorrecto: "))
rb = int(input("Ingresa el puntaje en blanco: "))

# Cálculo de puntajes
prc = rc * 3
pri = ri * -1
prb = rb * 0
pf = prc + pri + prb

# Impresión del resultado final
print("El puntaje final es:", pf)