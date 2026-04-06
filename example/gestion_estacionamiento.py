class Vehiculo:
    def __init__(self, patente, tipo):
        self.patente = patente
        self.tipo = tipo  
        self.tarifa = 1500 if tipo == "Automovil" else 2200

    def mostrar_datos(self):
        return f"Vehículo [{self.patente}] - Tipo: {self.tipo} - Tarifa/h: ${self.tarifa}"