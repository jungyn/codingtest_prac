n, k = map(int, input().split())

result = 1
for i in range(k):
    result *= n
    n -= 1

div = 1
for j in range(k, 0, -1):
    div *= j

print(result // div)