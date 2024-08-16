N = int(input())

coin = [500, 100, 50, 10, 5, 1]
money = 1000 - N
count = 0

for i in coin:
  count += money // i
  money = money % i

print(count)