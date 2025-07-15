class Celular:
    def __init__(self, marca, color, tamaño, memoria):
        self.marca = marca
        self.color = color
        self.tamaño = tamaño
        self.memoria = memoria
        self.encendido = False

    def prender(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} está ahora encendido.")
        else:
            print(f"{self.marca} ya está encendido.")

