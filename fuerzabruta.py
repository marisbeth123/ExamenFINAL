import sys
import time
from itertools import permutations

distancias = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 18],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 12],
    [25, 18, 20, 12, 0]
]

def resolver_tsp_fuerza_bruta(matriz):
    n = len(matriz)
    ciudades_restantes = list(range(1, n))
    costo_minimo = sys.maxsize
    mejor_ruta = []

    for perm in permutations(ciudades_restantes):
        costo_actual = 0
        ciudad_actual = 0
        
        for proxima_ciudad in perm:
            costo_actual += matriz[ciudad_actual][proxima_ciudad]
            ciudad_actual = proxima_ciudad
        
        costo_actual += matriz[ciudad_actual][0]
        
        # Si encontramos una ruta mejor, la guardamos
        if costo_actual < costo_minimo:
            costo_minimo = costo_actual
            mejor_ruta = [0] + list(perm) + [0]
            
    return costo_minimo, mejor_ruta
inicio = time.perf_counter()
costo, ruta = resolver_tsp_fuerza_bruta(distancias)
fin = time.perf_counter()

print("=== ENFOQUE: FUERZA BRUTA ===")
print(f"Costo mínimo: {costo} km")
print(f"Ruta óptima: {' -> '.join(map(str, ruta))}")
print(f"Tiempo de ejecución: {(fin - inicio):.6f} segundos")
