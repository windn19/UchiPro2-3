array = list(range(1, 1000))
n = len(array)
x = 990
i1 = 3

for i in range(n):
    i1 += 1
    if x == array[i]:
        print(i)
        i1 += 2
        break
    i1 += 1
else:
    i1 += 1
    print(-1)
print(i1)
