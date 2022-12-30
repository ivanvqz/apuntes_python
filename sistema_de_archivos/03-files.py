# archivo = open('archivo.txt', 'r')
# print(archivo.read())
# archivo.close()#es importante cerrar el archivo

# archivo = open('archivo.txt', 'a')#a = append
# # recorrer lineas
# # for linea in archivo:
#     # print(linea, end='')#end quita los saltos de linea
#     #editar el archivo
# archivo.write('\neditando mi documento')
# archivo.close()

# for para añadir múltiples lineas
archivo = open('archivo.txt', 'w')
for linea in range(1, 10):
    archivo.write('\nTexto: ' + str(linea))
archivo.close()