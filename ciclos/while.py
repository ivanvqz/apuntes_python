#tabla de multiplicar
#se declara la variable
# numero = int(input("Digite un número: "))
# #inicializar iterador
# i = 1
# while i<=10:
#     print(numero, "x", i, "=", numero*i)
#     i += 1

#mostrar la sumatoria de numeros hasta que se introduzca el cero
# i = 0
# numero = int(input("Introduzca un numero: "))
# while numero != 0:
#     i+=numero
#     numero = int(input("Introduzca un numero: "))
# print("La suma de los numeros es: ", i)

#leer numeros enteros hasta que se ingrese cero, y mostrar la sumatoria de los 
# numeros positivos
#se inicializan los contadores
positivos = 0
i = 0
#se crea una variable para leer el numero
numero = int(input("Introduzca un numero: "))

#Mientras el numero sea diferente de cero, se suma el numero
while numero != 0:
    #si el numero es posiivo, al contador positivo se le va a sumar uno
    if numero > 0:
        positivos+=1
    #se repite el proceso
    numero = int(input("Introduzca otro numero: "))
#se imprime la suma de los numeros positivos
print("La cantidad de numeros positivos es: ", positivos)