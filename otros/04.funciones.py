# def saludar(nombre, edad, **diccionario):#*opcionales es una tupla
#     # nombre = input("¿Cómo te llamas? ")
#     # edad = int(input("¿En qué año naciste? "))
#     print(f'¡Hola {nombre}!.\nTienes {2020 - edad} años.\nRestantes= {diccionario}')
# saludar('Ivan', 2002, nombre='Ivan', edad=2002, otro='otro')

#retornar valores
def asignar_calor(x, y):
    x += 1
    y *= 1
    return x, y#añade los valores a una tupla y devuelve un solo valor
variable = asignar_calor(2, 5)
print(variable)