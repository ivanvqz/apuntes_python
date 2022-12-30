#recorrer diccionarios en python
datonumeros_telefonicos = {'Ivan':'123456789', 'Pedro':'987654321', 'Juan':'123456789'}
print(type(datonumeros_telefonicos))
for clave, valor in datonumeros_telefonicos.items():#items es una funcion de diccionarios que permite recorrerlos
    print(f'Nombre: {clave}.\nNumero: {valor}\n')
    
#recorrer cadenas de texto
mensaje = 'aprendiendo pyton'
for letra in mensaje:
    print(letra)
    
#recorrer rangos
for var in range(1, 10):
    print(var)