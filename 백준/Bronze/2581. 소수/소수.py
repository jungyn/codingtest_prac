m = int(input())
n = int(input())

ss = []
for i in range(m, n+1):
    for j in range(1, int(i**1/2)+1):
        if i%j==0:
            ss.append(i)

dict = {}
for num in ss:
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1

hap = 0
list = []
for i in dict:
    if dict[i] == 1:
        hap += i
        list.append(i)
if list:
    print(hap)
    print(list[0])
else:
    print(-1)