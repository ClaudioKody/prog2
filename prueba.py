# Clase Astronauta (Encapsulamiento)
class Astronauta:
    def __init__(self, nombre, edad):
        self.__nombre = nombre      # atributo privado
        self.__edad = edad          # atributo privado

    # getters
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    # setter
    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad


# Clase base Nave
class Nave:
    def __init__(self, nombre):
        self.nombre = nombre

    def despegar(self):
        print(f"La nave {self.nombre} está despegando...")


# Clases hijas (Polimorfismo)
class NaveTripulada(Nave):
    def despegar(self):
        print(f"La nave tripulada {self.nombre} despega con astronautas 🚀")


class NaveCarga(Nave):
    def despegar(self):
        print(f"La nave de carga {self.nombre} transporta suministros 📦")


# Clase Mision
class Mision:
    def __init__(self, nombre, nave):
        self.nombre = nombre
        self.nave = nave

    def iniciar_mision(self):
        print(f"Iniciando misión: {self.nombre}")
        self.nave.despegar()   # polimorfismo en acción


# 🔹 Ejemplo de uso
astro = Astronauta("Tomy", 19)

nave1 = NaveTripulada("Orion")
nave2 = NaveCarga("CargoX")

mision1 = Mision("Artemis I", nave1)
mision2 = Mision("Artemis II", nave2)

mision1.iniciar_mision()
mision2.iniciar_mision()