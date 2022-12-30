# Escribe un programa que tome cada cuatro horas la temperatura exterior, leyéndola
# en un periodo de 24 horas. Es decir, debe leer 6 temperaturas. Calcule la temperatura media 
# del día, la temperatura más alta y la mas baja


try:
    
    mayor = 0
    menor = 99
    sumaTotal = 0
    promedio = 0
    
    for i in range(0, 25):
        temperatura = input(float(print(f'Introduzca la temperatura de la hora: {i}')))
        
        sumaTotal += temperatura #se irá iterando la suma para sacar el promedio
        
        if temperatura > mayor:
            mayor == temperatura #se asigna el mayor valor
        
        if temperatura < menor:
            menor == temperatura # si es menor se le asigna a este numero
        i += 4
            
    print(f'Temperatura promedio: {promedio}')
    print(f'Temperatura más alta: {mayor}')
    print(f'Temperatura más baja: {menor}')
except:
    print(f'Error, introduzca un valor válido.')