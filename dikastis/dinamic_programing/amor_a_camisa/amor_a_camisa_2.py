quantity_sectors = int(input(""))
quantity_fans_per_sector_string = input("")

quantity_fans_per_sector = [
    int(quantity_fans_string) for quantity_fans_string in quantity_fans_per_sector_string.split(" ")
]

sectors_graph = {}

for i in range(quantity_sectors):
    sector = quantity_fans_per_sector[i]

    prev_neighborhood_position = i - 1
    next_neighborhood_position = i + 1

    chain = [
        quantity_fans_per_sector[j] for j in range(i + 1, quantity_sectors) if j != prev_neighborhood_position and j != next_neighborhood_position
    ]

    already_exits = sectors_graph.get(sector)

    if already_exits:
        sectors_graph[sector] = sectors_graph[sector] + chain
    else:
        sectors_graph[sector] = chain

print(sectors_graph)
max_fans_photographed = -1
max_steps = quantity_sectors // 2