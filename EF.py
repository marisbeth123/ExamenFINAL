import sys
import time


distancias = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 18],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 12],
    [25, 18, 20, 12, 0]
]

N = len(distancias)
# Tabla de memoización: 2^N máscaras posibles x N ciudades
memo = [[-1] * N for _ in range(1 << N)]
ruta_siguiente = [[-1] * N for _ in range(1 << N)]

def resolver_tsp_pd(mask, u):
    
    if mask == (1 << N) - 1:
        return distancias[u][0]
    
    if memo[mask][u] != -1:
        return memo[mask][u]
    
    costo_minimo = sys.maxsize
    mejor_vecino = -1
    
    for v in range(N):
       
        if (mask & (1 << v)) == 0:
            nuevo_costo = distancias[u][v] + resolver_tsp_pd(mask | (1 << v), v)
            if nuevo_costo < costo_minimo:
                costo_minimo = nuevo_costo
                mejor_vecino = v
                
    memo[mask][u] = costo_minimo
    ruta_siguiente[mask][u] = mejor_vecino
    return costo_minimo

def reconstruir_ruta():
    camino = [0]
    mask = 1
    u = 0
    while True:
        v = ruta_siguiente[mask][u]
        if v == -1:
            break
        camino.append(v)
        mask |= (1 << v)
        u = v
    camino.append(0)
    return camino
inicio = time.perf_counter()
costo_optimo = resolver_tsp_pd(1, 0)
ruta_optima = reconstruir_ruta()
fin = time.perf_counter()

print("=== ENFOQUE: PROGRAMACIÓN DINÁMICA ===")
print(f"Costo mínimo: {costo_optimo} km")
print(f"Ruta óptima: {' -> '.join(map(str, ruta_optima))}")
print(f"Tiempo de ejecución: {(fin - inicio):.6f} segundos")