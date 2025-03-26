L = int(input())
alpha = input()
alist = []
answer = 0

for i in alpha:
    alist.append(ord(i) - 96)

for n in range(L):
    answer += alist[n] * 31**n
print(answer % 1234567891)