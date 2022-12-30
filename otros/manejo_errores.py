# try:
#     #ingresar numeros
#     num1 = int(input("Ingrese un numero: "))
#     num2 = int(input("Ingrese otro numero: "))
#     sumar = num1 + num2
#     print(f'La suma de {num1} y {num2} es {sumar}')
# except:#se ejecuta cuando hay un error de código
#     print('Error, introduzca un número válido.')

#error ZeroDivisionError
# try:
#     num1 = int(input("Ingrese un numero: "))
#     num2 = int(input("Ingrese otro numero: "))
#     division = num1 / num2
#     print(f'La suma de {num1} y {num2} es {division}')
# except ZeroDivisionError:
#     print('No se puede divirir para cero')
# finally:
#     print('Fin del programa')

#name error
# try:
#     print(nombre)
# except NameError:
#     print('No existe la variable nombre')

#type error o cuando se introducen dos tipos de datos distintos
try:
    numero = 2
    texto = 'Bienvenido'
    suma = numero + texto
except TypeError as error:#se guarda como variable error el mensaje de error
    print(f'El error es: {str(error)}')