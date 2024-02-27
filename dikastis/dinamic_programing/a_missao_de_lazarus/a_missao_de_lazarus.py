planets_string = input("").strip()

planets = planets_string.split(', ') if planets_string != '' else []
sorted_planets = sorted(planets)
quantity_planets = len(sorted_planets)

def generate_ways(list, i, memo):
    if i > len(list) - 1:
        return

    has_memo = memo.get(i)

    if has_memo:
        return has_memo

    next_position = i + 1

    has_next_planet = i < len(list) - 1

    planet = list[i]

    if not has_next_planet:
        ways = [[planet]]
        memo[i] = ways

        return ways

    ways = [[planet]]

    for j in range(next_position, len(list)):
        ways_next_planet = generate_ways(list, j, memo)

        for way_next_planet in ways_next_planet:
            ways.append([planet] + way_next_planet)

    memo[i] = ways

    return ways

dp = {}
generate_ways(sorted_planets, 0, dp)

result = [[]]

for i in range(quantity_planets):
    ways = dp.get(i)

    result = result + ways

print('O número de subsets de visitação é', len(result))
print('São eles:', result)
