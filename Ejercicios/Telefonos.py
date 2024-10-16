while True:
    tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")

    print (len(tel))
    # Imprime el valor ingresado
    print("Valor ingresado:", tel)
    
    # Imprime la longitud de la entrada
    print("Longitud de la entrada:", len(tel))

    # Verifica que la longitud sea suficiente para analizar
    if len(tel) >= 17:
        # Imprime cada parte relevante para la depuración
        print("Tercer carácter:", tel[3])  # Debería ser un guion '-'
        print("Dígitos del 4 al 13:", tel[4:14], "¿Es dígito?", tel[4:14].isdigit())
        print("Carácter en la posición 14:", tel[14])  # Debería ser un guion '-'
        print("Dígitos desde la posición 15:", tel[15:], "¿Es dígito?", tel[15:].isdigit())

    # Verifica si el formato es correcto
    if (len(tel) == 17 and 
        tel[0] == '+' and 
        tel[3] == '-' and 
        tel[4:14].isdigit() and  # Asegúrate de incluir el índice correcto
        tel[14] == '-' and 
        tel[15:].isdigit()):
        
        print('Validación exitosa.')
        print('El número de teléfono es:', tel[4:-3])  # Extrae la parte del número
        break  # Sale del bucle si la entrada es válida
    else:
        print("El formato del número de teléfono es incorrecto. Asegúrate de usar el formato +xx-xxxxxxxxx-xx.")
        print("Valores analizados:")
        print("tel[0:3]:", tel[0:3])  # Imprime los primeros tres caracteres
        print("tel[3]:", tel[3])      # Imprime el carácter en la posición 3
        print("tel[4:14]:", tel[4:14])  # Imprime los dígitos del 4 al 13
        print("tel[14]:", tel[14])    # Imprime el carácter en la posición 14
        print("tel[15:]:", tel[15:])   # Imprime desde la posición 15 en adelante
