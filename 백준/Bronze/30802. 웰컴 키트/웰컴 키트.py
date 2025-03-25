n = int(input())
sizes = map(int, input().split())
t, p = map(int, input().split())
tshirt = 0
for i in sizes:
    if i % t == 0:
        tshirt += i//t
    else:
        tshirt += i//t + 1

print(tshirt)
print(n // p, n % p)