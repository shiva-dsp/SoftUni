from collections import deque

nodes = int(input())

graph = {}

for _ in range(nodes):
    line_parts = input().split('->')
    node = line_parts[0].strip()
    children = line_parts[1].strip().split(', ') if line_parts[1] else []
    graph[node] = children

visited = set()
cycles = set()


def dfs(node, graph, visited, sorted_nodes):
    if node in cycles:
        raise Exception('Cycle has been detected. Invalid topological sorting.')
    if node in visited:
        return

    visited.add(node)
    cycles.add(node)
    for child in graph[node]:
        dfs(child, graph, visited, sorted_nodes)

    cycles.remove(node)
    sorted_nodes.append(node)


sorted_nodes = deque()
for node in graph:
    dfs(node, graph, visited, sorted_nodes)

print(*sorted_nodes, sep=' ')