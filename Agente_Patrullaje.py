import random
import time

ruta_patrullaje = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2)]
obstaculos = [(1, 2), (3, 2)]
direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Agente:
    def __init__(self, ruta, obstaculos):
        self.ruta = ruta
        self.posicion = ruta[0]
        self.obstaculos = obstaculos
        self.indice_ruta = 0

    def detectar_obstaculo(self):
        siguiente_posicion = self.ruta[self.indice_ruta + 1] if self.indice_ruta + 1 < len(self.ruta) else self.posicion
        if siguiente_posicion in self.obstaculos:
            return True
        return False

    def cambiar_direccion(self):
        direccion_aleatoria = random.choice(direcciones)
        print(f"Agente cambia de dirección aleatoriamente: {direccion_aleatoria}")

    def mover(self):
        if self.detectar_obstaculo():
            self.cambiar_direccion()
            direccion = random.choice(direcciones)
            self.posicion = (self.posicion[0] + direccion[0], self.posicion[1] + direccion[1])
            print(f"El agente se mueve a una nueva posición debido a un obstáculo: {self.posicion}")
        else:
            self.indice_ruta += 1
            if self.indice_ruta < len(self.ruta):
                self.posicion = self.ruta[self.indice_ruta]
            print(f"El agente se mueve a: {self.posicion}")

agente = Agente(ruta_patrullaje, obstaculos)

for _ in range(10):
    agente.mover()
    time.sleep(1)
