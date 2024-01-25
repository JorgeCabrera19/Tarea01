A = float(input("Ingrese el valor de la variable A"))
B = float(input("Ingrese el valor de la variable B"))
C = float(input("Ingrese el valor de la variable C"))

raiz = float(((B*B)-4*A*C)**0.5)

pos = float((-B + raiz)/2*A)

neg = float((-B - raiz)/2*A)

print("Los resultados son x:", pos, "x2:", neg)