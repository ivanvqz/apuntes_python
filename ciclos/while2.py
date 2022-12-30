# while condicion:
#     #codigo
contador = 0
while True:
    contador += 2
    if contador > 100:
        break
    elif contador == 50:
        print('Llegaste a la mitad')
        continue #se salta el resto del ciclo y ejecuta la línea de código
    else:
        print(contador)
print('Fin del programa')