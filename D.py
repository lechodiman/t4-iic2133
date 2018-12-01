''' Highway Decomission '''

from collections import defaultdict
from heapq import heappop, heappush


def dijkstra(edges, f):
    g = defaultdict(list)
    for l, r, c, money in edges:
        g[l].append((c, money, r))

    q, seen, mins, mins_money = [(0, 0, f, ())], set(), {f: 0}, {f: 0}
    while q:
        # pprint(mins_money)

        (cost, money, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)

            # if v1 == t:
            #     return (cost, money, path)

            for c, mon, v2 in g.get(v1, ()):
                if v2 in seen:
                    continue
                prev = mins.get(v2, None)
                next = cost + c

                prev_money = mins_money.get(v2, None)
                next_money = money + mon

                if prev is None or next < prev:
                    mins[v2] = next
                    mins_money[v2] = next_money
                    heappush(q, (next, next_money, v2, path))

                elif prev_money is not None and next == prev and\
                        next_money < prev_money:
                    # desempatar con el money
                    mins[v2] = next
                    mins_money[v2] = next_money
                    heappush(q, (next, next_money, v2, path))

    return max([v for k, v in mins_money.items()])

    # return float("inf")


def main():
    # init graph
    n, m = (int(x) for x in input().split(' '))

    edges = []

    for i in range(m):
        from_node, to_node, distance, cost = (int(x) for x in input().split(' '))

        edges.append((from_node, to_node, distance, cost))
        edges.append((to_node, from_node, distance, cost))

    # pprint(edges)

    print(dijkstra(edges, 1))


if __name__ == '__main__':
    main()
