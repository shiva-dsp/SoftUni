from collections import deque


def dfs(node, graph, visited, result):
    if node in visited:
        return

    visited.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, result)

    result.appendleft(node)


graph = {}

while True:
    line = input()
    if line == 'End':
        break
    node, children_str = [x.strip() for x in line.split('->')]
    children = children_str.split()
    graph[node] = children

visited = set()
result = deque()
for node in graph:
    dfs(node, graph, visited, result)

print(' '.join(result))

# ------------- tests --------------

# Mort -> Time Space
# Time -> Future Robot
# Space -> Metro
# Future -> Space Metro
# Robot -> Future
# Metro ->
# End

# By -> The
# Story -> The Told
# Told -> Narrator
# The -> Narrator Ever Greatest
# Narrator ->
# Some -> Told Ever
# Greatest ->
# Ever ->
# End

# --------- results ----------

# Mort Time Robot Future Space Metro

# Some Story Told By The Greatest Ever Narrator