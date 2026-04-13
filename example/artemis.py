#Clase Padre
class Vehiculo:
    def __init__(self, marca, modelo, nombre):
        self.marca = marca
        self.modelo = modelo
        self.nombre = nombre
    
    def encender(self):
        return f"{self.nombre} encendido"
    
    def info(self):
        return f"{self.nombre} - {self.marca} {self.modelo}"

#Clase Hija
class Cohete(Vehiculo):
    def __init__(self, marca, modelo, nombre, mision):
        super().__init__(marca, modelo, nombre)
        self.mision = mision
    
    def lanzar(self):
        return f"{self.nombre} despegando en la misión {self.mision}"
    
    def estacionar(self):
        return f"{self.nombre} acoplado en la estación espacial"
    
    def explotar(Self):
        return f"{self.nombre} Explotando capsula" 