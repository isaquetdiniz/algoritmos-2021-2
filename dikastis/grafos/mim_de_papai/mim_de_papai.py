import sys


class Graph:
    def __init__(self, v):
        self.graph = {}

        for i in range(1, v + 1):
            self.graph[i] = []

    def add_edge(self, u, v):
        edge_exists = self.graph.get(u)

        if not edge_exists:
            self.graph[u] = [v]
            return

        edge_exists.append(v)

    def count_connections(self, origin):
        visited = set()

        self.dfs_util(origin, visited)

        return len(visited)

    def dfs_util(self, v, visited):
        visited.add(v)

        neighbors = self.graph.get(v)

        if not neighbors:
            return

        for neighbor in neighbors:
            if neighbor and neighbor not in visited:
                self.dfs_util(neighbor, visited)
lines = 0

for line in sys.stdin:
    lines += 1
    [user_1, user_2] = [int(num_str) for num_str in line.split()]

    if lines == 1:
        graph = Graph(user_1)
        continue

    [user_1, user_2] = [int(num_str) for num_str in line.split()]

    graph.add_edge(user_1, user_2)
    graph.add_edge(user_2, user_1)


output = ''
for user in graph.graph.keys():
    output += str(graph.count_connections(user)) + ' '

print(output[:-1])
