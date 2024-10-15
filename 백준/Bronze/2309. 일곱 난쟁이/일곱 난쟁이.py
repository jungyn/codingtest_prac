list = []
for _ in range(9):
    n = int(input())
    list.append(n)
list.sort()

nmg = sum(list)-100
arr = []
for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i] + list[j] == nmg:
            val1 = list[i]
            val2 = list[j]
list.remove(val1)
list.remove(val2)

for li in list:
    print(li)