from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, distance):
        self.first = first
        self.second = second
        self.distance = distance

    def __gt__(self, other):
        return self.distance > other.distance


def calc_damage(jumps, damage):
    for _ in range(jumps):
        damage //= 2

    return damage


def prim(node, damage, damage_by_node, graph):
    damage_by_node[node] += damage

    tree = {node}
    jumps = [0] * len(graph)

    pq = PriorityQueue()
    [pq.put(edge) for edge in graph[node]]

    while not pq.empty():
        min_edge = pq.get()

        tree_node, non_tree_node = -1, -1

        if min_edge.first in tree and min_edge.second not in tree:
            tree_node, non_tree_node = min_edge.first, min_edge.second
        elif min_edge.second in tree and min_edge.first not in tree:
            tree_node, non_tree_node = min_edge.second, min_edge.first

        if non_tree_node == -1:
            continue

        tree.add(non_tree_node)
        [pq.put(edge) for edge in graph[non_tree_node]]

        jumps[non_tree_node] = jumps[tree_node] + 1
        damage_by_node[non_tree_node] += calc_damage(jumps[non_tree_node], damage)


nodes = int(input())
edges = int(input())
lightnings = int(input())

graph = {node: [] for node in range(nodes)}

for _ in range(edges):
    first, second, distance = [int(x) for x in input().split()]
    edge = Edge(first, second, distance)
    graph[first].append(edge)
    graph[second].append(edge)

damage_by_node = [0] * nodes

for _ in range(lightnings):
    node, damage = [int(x) for x in input().split()]
    prim(node, damage, damage_by_node, graph)

print(max(damage_by_node))

# ------------- tests --------------

# 5
# 5
# 2
# 0 1 10
# 1 4 20
# 2 4 30
# 0 2 35
# 0 3 50
# 0 40
# 4 20

# 10
# 8
# 3
# 0 1 5
# 1 2 4
# 1 3 6
# 2 3 3
# 2 5 7
# 2 4 2
# 7 6 8
# 7 8 1
# 2 100
# 0 200
# 9 100

# --------- results ----------

# 45

# 225