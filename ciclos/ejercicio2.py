# Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
mayor = -1
#el  -1 es porque el mayor numero es el 0
numero = int(input("Ingrese un numero positivo: "))
#mientras el numero sea mayor a cero
while numero>=0:
    #se compara si el numero es mayor a mayor
    if numero > mayor:
        #se crea una variable mayor y se le asigna el numero que sea mayor
        #y se comparan
        mayor = numero
    numero = int(input("Ingrese otro numero positivo: "))
print("El numero mayor es: ", mayor)