def quicksort(list):
    if len(list) < 2:
        return list

    pivot = list[0]
    smaller = [i for i in list[1:] if i <= pivot]
    biggest = [i for i in list[1:] if i > pivot]

    return quicksort(smaller) + [pivot] + quicksort(biggest)

quantity_lines = int(input())

for i in range(quantity_lines):
    input_grades = input().split()

    grades = [float(grade_string) for grade_string in input_grades]

    grades_sorted = quicksort(grades)

    median = round((grades_sorted[1] + grades_sorted[2]) / 2, 1)
    mean = round(sum(grades_sorted) / 4, 1)

    print(max(median, mean))