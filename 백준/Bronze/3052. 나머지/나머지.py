nmg = []
for i in range(10):
    n = int(input())
    nmg.append(n % 42)
print(len(set(nmg)))