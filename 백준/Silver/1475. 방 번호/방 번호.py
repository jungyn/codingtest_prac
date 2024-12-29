room = input()

num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in room:
    num[int(i)] += 1
if num[6] < num[9]:
    while num[9] > num[6]:
        num[9] -= 1
        num[6] += 1
elif num[6] > num[9]:
    while num[9] < num[6]:
        num[9] += 1
        num[6] -= 1
print(max(num))