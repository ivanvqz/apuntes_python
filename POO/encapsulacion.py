class Usuario:
    #constructor
    def __init__(self, nombre: str, edad: int):
        self.__nombre = nombre
        self.__edad = edad
    # getters y setters
    # métodos para que el usuario pueda acceer y modificar los atributos
    
    ##getters: permiten obtener el valor de un atributo fuera de la clase
    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
    
    #setters: permiten modificar el valor de un atributo fuera de la clase
    def setNombre(self, nombre: str):
        self.__nombre = nombre
        return self.__nombre
    
    def setEdad(self, edad: int):
        self.__edad = edad
        return self.__edad
    
    
    # def __registrar(self):
    #     print(f"Registrando {self.nombre}, con la edad de {self.edad}")
    
    # def __info(self):
    #     print(f"Información del usuario:\nNombre: {self.__nombre}, Edad: {self.__edad}")
        
    # def __str__(self) -> str:
    #     return f"Nombre: {self.__nombre}, Edad: {self.__edad}"
    
    # def permisos(self):
    #     self.__info()
    #     print("Permisos de usuario")
        
usuario = Usuario("Ivan", 23)
print(usuario.setNombre("Ivan"))
print(usuario.setEdad(23))
# print(usuario.getNombre())
# print(usuario.getEdad())