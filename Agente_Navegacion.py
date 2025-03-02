import heapq

class NavegadorLaberinto:
    def __init__(self, laberinto, inicio, meta):
        self.laberinto = laberinto
        self.inicio = inicio
        self.meta = meta
        self.filas = len(laberinto)
        self.columnas = len(laberinto[0])

    def heuristica(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def encontrar_ruta(self):
        conjunto_abierto = []
        heapq.heappush(conjunto_abierto, (0, self.inicio))
        recorrido = {}
        costo_g = {self.inicio: 0}
        costo_f = {self.inicio: self.heuristica(self.inicio, self.meta)}
        
        while conjunto_abierto:
            _, actual = heapq.heappop(conjunto_abierto)
            
            if actual == self.meta:
                return self.reconstruir_ruta(recorrido)
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                vecino = (actual[0] + dx, actual[1] + dy)
                
                if 0 <= vecino[0] < self.filas and 0 <= vecino[1] < self.columnas and self.laberinto[vecino[0]][vecino[1]] == 0:
                    nuevo_costo_g = costo_g[actual] + 1
                    
                    if vecino not in costo_g or nuevo_costo_g < costo_g[vecino]:
                        recorrido[vecino] = actual
                        costo_g[vecino] = nuevo_costo_g
                        costo_f[vecino] = nuevo_costo_g + self.heuristica(vecino, self.meta)
                        heapq.heappush(conjunto_abierto, (costo_f[vecino], vecino))
        
        return None

    def reconstruir_ruta(self, recorrido):
        ruta = []
        actual = self.meta
        while actual in recorrido:
            ruta.append(actual)
            actual = recorrido[actual]
        ruta.append(self.inicio)
        return ruta[::-1]

# Laberinto (0 = camino, 1 = pared)
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

inicio = (0, 0)
meta = (4, 4)

navegador = NavegadorLaberinto(laberinto, inicio, meta)
ruta = navegador.encontrar_ruta()

if ruta:
    print("Ruta encontrada:", ruta)
else:
    print("No hay camino disponible.")
