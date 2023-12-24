import sys


class HashTable:
    def __init__(self):
        self.values = [[] for i in range(11)]

    def add(self, key, value):
        self.values[key].append(value)

    def print(self):
        result = []

        for i in range(1, 11):
            value = self.values[i]

            if not len(value):
                continue

            value.sort()

            partial = []
            for player in value:
                partial.append(player)

                if len(partial) == i:
                    result.append(partial)
                    partial = []

        print(result)

hash_table = HashTable()

for line in sys.stdin:
    [player, team_size_string] = line.split()

    team_size = int(team_size_string)

    hash_table.add(team_size, player)

hash_table.print()