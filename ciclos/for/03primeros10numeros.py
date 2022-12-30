# Realiza un programa que calcule y muestre en la salida la suma de los cuadrados de los 
# primeros diez numeros enteros mayores de cero
suma = 0
cuadrado = 0
for i in range(1, 11):
    cuadrado = i * i #los cuadrados se irán iterando con cada repeición del ciclo
    suma += cuadrado #suma = suma  + cuadrado
print(f'La suma de todos los valores es: {suma}')