import random

class MapExplorer:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.map = [[0 for _ in range(cols)] for _ in range(rows)]
        self.visited = set()  
        self.position = (0, 0) 
        self.visited.add(self.position)

    def get_neighbors(self, pos):
        x, y = pos
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, Abajo, Izquierda, Derecha
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < self.rows and 0 <= new_y < self.cols:
                if (new_x, new_y) not in self.visited:
                    neighbors.append((new_x, new_y))
        
        return neighbors
    
    def move(self):
        """ Mueve el agente a una celda no visitada."""
        neighbors = self.get_neighbors(self.position)
        
        if neighbors:
            self.position = random.choice(neighbors)
            self.visited.add(self.position)
        else:
            print("No hay más movimientos disponibles.")

    def explore(self, steps=50):
        for _ in range(steps):
            self.move()
            print(f"Agente en posición: {self.position}")

# Ejemplo de uso
explorer = MapExplorer(5, 5)  # Crear un entorno de 5x5
explorer.explore(20)  # Explorar durante 20 pasos
