class Max_Heap:
    def __init__(self, vector, size_total):
        self.size_total = size_total
        self.size = size_total
        self.vector = vector

        for i in range(self.size_total // 2, 0, -1):
            self.max_heapify(i)


    def parent(self, i):
        return i // 2

    def left(self, i):
        return 2 * i

    def right(self, i):
        return (2*i) + 1

    def change(self, i, j):
        aux = self.vector[i]
        self.vector[i] = self.vector[j]
        self.vector[j] = aux

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)

        if l <= self.size and self.vector[l] > self.vector[i]:
            maior = l
        else:
            maior = i

        if r <= self.size and self.vector[r] > self.vector[maior]:
            maior = r

        if maior != i:
            self.change(i, maior)
            self.max_heapify(maior)

vector = [0] * 21
for i in range(1, 21):
    vector[i] = (2 * i * i) - (10 * i)

print(vector)
max_heap = Max_Heap(vector, 20)
print(max_heap.vector)
print(max_heap.size_total)
print(max_heap.size)