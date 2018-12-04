import sys
from collections import defaultdict, deque

def dfs_paths(graph, start, goal, busc, costos, costo_total):
    costo_camino = 0
    stack = deque()
    stack.append(start)
    visited = set()
    while stack:
        vertex = stack.pop()
        print(vertex)
        if not busc[vertex]:
            costo_total += costos[vertex]
            busc[vertex] = True
        costo_camino += costos[vertex]
        if vertex not in visited:
            if vertex == goal:
                return costo_camino, costo_total
            visited.add(vertex)
            for neighbor in graph[vertex]:
                stack.append(neighbor)

def main():
    costo_total = 0
    costos = {1:0}
    graph = defaultdict(list)
    busc = {}
    iniciales = [int(x) for x in input().split(' ')]
    for i in range(iniciales[0] - 1):
        lista= [int(x) for x in input().split(' ')]
        costos[lista[1]] = lista[2]
        graph[lista[1]].append(lista[0])
        busc[lista[1]] = False
        busc[lista[0]] = False
    maximo = 0
    buscados = [int(x) for x in input().split(' ')]
    for i in range(iniciales[1]):
        if not busc[buscados[i]]:
            path = dfs_paths(graph, buscados[i], 1,  busc, costos, costo_total)
            if path[0] > maximo:
                maximo = path[0]
            costo_total = path[1]
        else:
            continue
    return costo_total - maximo

if __name__ == "__main__":
    print(main())
