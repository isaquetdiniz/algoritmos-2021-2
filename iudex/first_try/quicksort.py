vector = [90,40,20,30,10,2,3,6,100, 65, 12, 56, 13, 577, 1]

def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp


    return rightmark

def quickSortHelper(alist,first,last):
    if first<last:
        aux = alist[first]
        alist[first] = alist[4]
        alist[4] = aux

        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def quickSort(alist, n):
    quickSortHelper(alist,0, n - 1)

quickSort(vector, 15)
print(vector)