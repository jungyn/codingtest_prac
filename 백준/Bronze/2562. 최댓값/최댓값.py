array = []
for i in range(9):
    n = int(input())
    array.append((i+1, n))

array.sort(key=lambda x:x[1])
print(array[-1][1])
print(array[-1][0])