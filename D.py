''' Highway Decommission'''

from queue import PriorityQueue


class Edge:
    def __init__(self, to, length, cost):
        self.to = to
        self.length = length
        self.cost = cost

    def __lt__(self, other):
        if self.length == other.length:
            return self.cost < other.cost
        return self.length < other.length

    def __repr__(self):
        return "Edge: to {}, l: {}, c: {}".format(self.to, self.length, self.cost)


def my_cmp(edge_1, edge_2):
    if (edge_1 < edge_2):
        # edge 1 has greater value, ie, more expensive
        return 1
    if (edge_2 < edge_1):
        return -1
    return 0


def main():
    # init graph
    n, m = (int(x) for x in input().split(' '))

    # list of lists of edges
    g = [[] for i in range(n)]

    for i in range(m):
        from_node, to_node, distance, cost = (int(x) for x in input().split(' '))
        from_node -= 1
        to_node -= 1

        g[from_node].append(Edge(to_node, distance, cost))
        g[to_node].append(Edge(from_node, distance, cost))

    # priority queue with edges
    q = PriorityQueue()
    q.put(Edge(0, 0, 0))

    # list of n best edges
    best = [Edge(0, float("inf"), float("inf")) for i in range(n)]
    best[0] = Edge(0, 0, 0)

    # list of cost
    cost = [0 for i in range(n)]

    while not q.empty():  # V times
        s = q.get()  # log E

        node = s.to

        if my_cmp(s, best[node]) == -1:
            continue

        for e in g[node]:  # E times
            to = e.to
            extra = Edge(to, s.length + e.length, e.cost)
            if my_cmp(extra, best[to]) == 1:
                best[to] = extra
                cost[to] = e.cost
                q.put(extra)  # Log E

    total = 0
    for i in range(n):
        total += cost[i]

    print(total)


if __name__ == '__main__':
    main()
