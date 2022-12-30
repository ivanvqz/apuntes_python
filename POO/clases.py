class Persona:
    #método inicializador que va a construir datos de nuestra clase
    def __init__(self, nombre, edad):#se va a ejecutar primero al crearse una instancia
        #self hace referencia a la clase actual, en este caso a la clase persona
        self.nombre = nombre
        self.edad = edad #se crean atributos de la clase persona
        
    #métodos
    def caminar(self):
        print(self.nombre + ' está caminando')
    
    def correr(self):
        print(self.nombre + ' está corriendo')
        
    #el metodo str permite retornar una cadena de texto
    def __str__(self):
        return 'Nombre: ' + self.nombre + ' Edad: ' + str(self.edad)

#instanciar objetos
persona = Persona('Ivan', 20) #primero se ejecuta init
print(persona) #se ejecuta el método str
persona.caminar() #se ejecuta el método caminar
