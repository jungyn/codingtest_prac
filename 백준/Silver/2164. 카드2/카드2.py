n = int(input())
from collections import deque

su = []

for i in range(1, n+1):
    su.append(i)

su = deque(su) # 시간초과 때문에 deque 사용

while len(su) > 1:
    su.popleft() # pop(0) 대신 popleft() 사용 -> 시간초과로 인해 
    temp = su.popleft()
    su.append(temp)
print(su[0])