archivo = open('si.txt', 'a')
entrada = input('¿Qué piensas?: ')
archivo.write('\n' + entrada)
print('Gracias por tu opinión')
archivo.close()