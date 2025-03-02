import heapq

class SelectorRuta:
    def __init__(self, entorno, inicio, meta):
        self.entorno = entorno
        self.inicio = inicio
        self.meta = meta
        self.filas = len(entorno)
        self.columnas = len(entorno[0])

    def evaluar_utilidad(self, posicion):
        return self.entorno[posicion[0]][posicion[1]]

    def seleccionar_mejor_ruta(self):
        cola_prioridad = []
        heapq.heappush(cola_prioridad, (-self.evaluar_utilidad(self.inicio), self.inicio))
        recorrido = {}
        utilidad_acumulada = {self.inicio: self.evaluar_utilidad(self.inicio)}
        
        while cola_prioridad:
            _, actual = heapq.heappop(cola_prioridad)
            
            if actual == self.meta:
                return self.reconstruir_ruta(recorrido)
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                vecino = (actual[0] + dx, actual[1] + dy)
                
                if 0 <= vecino[0] < self.filas and 0 <= vecino[1] < self.columnas:
                    nueva_utilidad = utilidad_acumulada[actual] + self.evaluar_utilidad(vecino)
                    
                    if vecino not in utilidad_acumulada or nueva_utilidad > utilidad_acumulada[vecino]:
                        recorrido[vecino] = actual
                        utilidad_acumulada[vecino] = nueva_utilidad
                        heapq.heappush(cola_prioridad, (-nueva_utilidad, vecino))
        
        return None

    def reconstruir_ruta(self, recorrido):
        ruta = []
        actual = self.meta
        while actual in recorrido:
            ruta.append(actual)
            actual = recorrido[actual]
        ruta.append(self.inicio)
        return ruta[::-1]

entorno = [
    [3, 1, 4, 2, 5],
    [2, 3, 1, 4, 2],
    [4, 2, 5, 1, 3],
    [1, 4, 2, 3, 5],
    [5, 1, 3, 2, 4]
]

inicio = (0, 0)
meta = (4, 4)

selector = SelectorRuta(entorno, inicio, meta)
ruta = selector.seleccionar_mejor_ruta()

if ruta:
    print("Ruta óptima:", ruta)
else:
    print("No hay camino disponible.")
