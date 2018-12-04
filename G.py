from collections import defaultdict, deque

class Componente:
    def __init__(self):
        self.numero_d = 0
        self.numero_p = 0
        self.valor = 0
        self.total = 0

def knapSack(W, n, componentes):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif componentes[i - 1].total <= w:
                K[i][w] = max(componentes[i - 1].valor + K[i-1][w-componentes[i - 1].total],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]

def crear_componentes(grafo, visitados, D, P, precios_d, precios_p):
    componentes_p = []
    componentes_d = []
    sp = 0
    sd = 0
    for i in range(D + P):
        if visitados[i]:
            continue
        else:
            visitados[i] = True
            componente = Componente()
            cola = deque()
            cola.append(i)
            while cola:
                actual = cola.popleft()
                if actual >= D:
                    componente.total += precios_p[actual - D]
                    componente.numero_p += 1
                else:
                    componente.total += precios_d[actual]
                    componente.numero_d += 1
                for i in grafo[actual]:
                    if not visitados[i]:
                        visitados[i] = True
                        cola.append(i)
        if componente.numero_p > componente.numero_d:
            componente.valor = componente.numero_p - componente.numero_d
            componentes_d.append(componente)
        else:
            componente.valor = componente.numero_d - componente.numero_p
            componentes_p.append(componente)
    return componentes_d, componentes_p

def main():
    grafo = defaultdict(set)
    visitados = {}
    datos = [int(x) for x in input().split(' ')]
    D = datos[0]
    P = datos[1]
    B = datos[3]
    precios_d = [int(x) for x in input().split(' ')]
    precios_p = [int(x) for x in input().split(' ')]
    for i in range(D + P):
        visitados[i] = False
    for i in range(datos[2]):
        datos_grafo = [(int(x) - 1) for x in input().split(' ')]
        grafo[datos_grafo[0]].add(datos_grafo[1] + D)
        grafo[datos_grafo[1] + D].add(datos_grafo[0])
    componentes = crear_componentes(grafo, visitados, D, P, precios_d, precios_p)
    vd = D +  knapSack(B, len(componentes[0]), componentes[0])
    vp = P +  knapSack(B, len(componentes[1]), componentes[1])
    return str(vd) + " " + str(vp)


if __name__ == "__main__":
    print(main())

#REFERENCIAS
# https://github.com/FeloVilches/Solutions-ACM-ICPC-2015-South-America/blob/master/E%20Exposing%20corruption.cpp
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# https://chococontest.wordpress.com/2015/11/23/solucionario-regional-south-america-2015/
