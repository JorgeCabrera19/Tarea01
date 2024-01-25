dato = input("Ingresa un dato: ")

try:
    entero = int(dato)
    print("El dato ingresado es de tipo entero (int).")
except ValueError:

    try:
        flotante = float(dato)
        print("El dato ingresado es de tipo flotante (float).")
    except ValueError:
        print("El dato ingresado es de tipo cadena (string).")
