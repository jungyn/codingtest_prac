n, m = map(int, input().split())

a = set()
b = set()
result = []

for _ in range(n):
    a.add(input())

for _ in range(m):
    b.add(input())

for i in a:
    if i in b:
        result.append(i)

print(len(result))
result.sort()
for i in result:
    print(i)