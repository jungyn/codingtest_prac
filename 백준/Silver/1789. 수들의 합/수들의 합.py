s = int(input())
num = 0

for i in range(1, s+1):
    s -= i
    if s < 0:
        break
    num += 1
print(num)