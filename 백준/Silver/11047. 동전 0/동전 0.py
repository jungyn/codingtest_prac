n, k = map(int, input().split())

list = []

for _ in range(n):
    money = int(input())
    list.append(money)

list.sort(reverse=True)

count = 0
for i in list:
    count += k // i
    k = k % i
    
print(count)