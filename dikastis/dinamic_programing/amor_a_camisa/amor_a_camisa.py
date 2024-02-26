quantity_sectors = int(input(""))
quantity_fans_per_sector_string = input("")

quantity_fans_per_sector = [
    int(quantity_fans_string) for quantity_fans_string in quantity_fans_per_sector_string.split(" ")
]

def better_choice(list, results, i):
    has_result = results[i]

    if has_result:
        return has_result

    next_possible_neighborhood_position = i + 2

    new_list = list[next_possible_neighborhood_position:]
    item = list[i]

    if not new_list:
        results[i] = item
        return item

    better = list[i] + max([better_choice(list, results, i) for i in range(next_possible_neighborhood_position, len(list))])
    results[i] = better

    return better


results = [None] * quantity_sectors

for i in range(len(quantity_fans_per_sector) - 1, -1, -1):
    better_choice(quantity_fans_per_sector, results,i)

print(max(results), 'torcedores podem ser fotografados.')