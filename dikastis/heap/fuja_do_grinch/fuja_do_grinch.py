class MaxHeap:
    def __init__(self, list):
        self.size = len(list)
        self.list = list

        for i in range(self.size // 2, -1, -1):
            self.max_heapify(i)

    def max_heapify(self, index):
        left = self.left_pos(index)
        right = self.right_pos(index)

        biggest = None

        if left < self.size and self.list[left] > self.list[index]:
            biggest = left
        else:
            biggest = index

        if right < self.size and self.list[right] > self.list[biggest]:
            biggest = right

        if biggest != index:
            tmp = self.list[index]
            self.list[index] = self.list[biggest]
            self.list[biggest] = tmp

            self.max_heapify(biggest)


    def parent_pos(self, index):
        return index // 2

    def left_pos(self, index):
        return 2 * index

    def right_pos(self, index):
        return 2 * index + 1

    def get_list(self):
        return self.list
    
    def get_pos(self, index):
        return self.list[index]

input_string = input()

input_splitted = input_string.split()

numbers = []

for ch in input_splitted:
    number = int(ch)
    numbers.append(number)

max_heap = MaxHeap(numbers)

print(f'Atenção, Grinch está indo atrás do cidadão de {max_heap.get_pos(0)} anos, e logo após isso ele vai atrás do cidadão de {input_splitted[0]} anos.')