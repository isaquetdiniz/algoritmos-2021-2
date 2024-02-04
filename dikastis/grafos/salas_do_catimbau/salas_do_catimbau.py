import sys


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        edge_exists = self.graph.get(u)

        if not edge_exists:
            self.graph[u] = [v]
            return

        edge_exists.append(v)

    def has_way(self, origin, target):
        visited = set()

        self.dfs_util(origin, visited, target)

        if target in visited:
            print('TESOURO :)')
        else:
            print('SEM TESOURO :(')

    def dfs_util(self, v, visited, target):
        visited.add(v)

        neighbors = self.graph.get(v)

        if not neighbors:
            return

        for neighbor in neighbors:
            if neighbor and neighbor not in visited:
                self.dfs_util(neighbor, visited, target)



graph = Graph()
room = 0

for line in sys.stdin:
    if line == 'Tesouro':
        graph.add_edge(room, None)
        continue

    keys = [int(num_str) for num_str in line.split()]

    for key in keys:
        graph.add_edge(room, key - 1)

    room += 1

graph.has_way(0, room)