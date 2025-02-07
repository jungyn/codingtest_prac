n = input()
total = 0

for i in range(len(n)):
    total += int(n[i])

if (total % 3 == 0) and ('0' in n):
    print(''.join(sorted(n)[::-1]))
else:
    print(-1)