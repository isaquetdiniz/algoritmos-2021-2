class ShifuHashTable:
    def __init__(self):
        self.values = ['vago' for i in range(10)]

    def get(self, value):
        mod_value = value % 10

        item = self.values[mod_value]

        if item == 'vago':
            return None

        return item

    def set(self, value):
        ascii_sum = 0
        for ch in value:
            ascii_sum += ord(ch)

        mod_value = ascii_sum % 10

        value_exists = self.get(ascii_sum)

        if value_exists:
            next_empty_position = self.get_next_empty_position(mod_value)

            self.values[next_empty_position] = value

            return

        self.values[mod_value] = value

    def get_next_empty_position(self, position):
        next_empty_position = position

        for i in range(position + 1, len(self.values)):
            if self.values[i] == 'vago':
                next_empty_position = i
                return next_empty_position

        for i in range(0, position):
            if self.values[i] == 'vago':
                next_empty_position = i
                return next_empty_position

        return next_empty_position

    def print(self):
        print(self.values)


input_string = input()

groups = []

new_group = []

for ch in input_string:
    if ch in new_group:
        groups.append(new_group)

        new_group = []
        new_group.append(ch)
    else:
        new_group.append(ch)

if len(new_group) > 0:
    groups.append(new_group)

shifu_hash_table = ShifuHashTable()

for group in groups:
    shifu_hash_table.set(group)

shifu_hash_table.print()