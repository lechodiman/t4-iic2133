''' Highway Decomission '''

from collections import defaultdict
from heapq import heappop, heappush
from pprint import pprint


def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l, r, c, money in edges:
        g[l].append((c, money, r))

    q, seen, mins = [(0, 0, f, ())], set(), {f: 0}
    while q:
        (cost, money, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t:
                return (cost, path)

            for c, money, v2 in g.get(v1, ()):
                if v2 in seen:
                    continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, money, v2, path))

    return float("inf")


def main():
    # init graph
    graph = Graph()
    n, m = (int(x) for x in input().split(' '))
    print(n, m)

    edges = []

    for i in range(m):
        from_node, to_node, distance, cost = (int(x) for x in input().split(' '))

        edges.append((from_node, to_node, distance, cost))
        edges.append((to_node, from_node, distance, cost))

        print(from_node, to_node, distance, cost)

    pprint(edges)

    # dijkstra(edges, 1)


if __name__ == '__main__':
    main()
