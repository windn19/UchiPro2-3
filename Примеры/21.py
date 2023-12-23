array = [1, 4, 0, 3, 2, 5, 6, 9, 7, 10]
n = len(array)
i1 = 2

for i in range(n - 1):
    for j in range(n - i - 1):
        i1 += 1
        if array[j] > array[j + 1]:
            i1 += 3
            array[j], array[j + 1] = array[j + 1], array[j]
        i1 += 1
print(array)
print(i1)
