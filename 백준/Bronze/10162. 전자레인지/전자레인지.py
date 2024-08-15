T = int(input())

time = [300, 60, 10]
if T % 10 != 0:
  print(-1)
else:
  for i in time:
    print(T // i, end=' ')
    T = T % i