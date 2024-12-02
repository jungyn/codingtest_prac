n, k = map(int, input().split())

from collections import deque

queue = deque([i for i in range(1, n+1)])
print('<', end='')
while True:
    for _ in range(k-1):
        queue.append(queue.popleft())
    print(queue.popleft(), end = '')
    if queue:
        print(', ', end='')
    else:
        break
print('>', end='')