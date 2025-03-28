from collections import deque
n = int(input())
queue = deque([i for i in range(1, n+1)])
bottom = []

for i in range(n-1):
    bottom.append(queue.popleft())
    queue.append(queue.popleft())

answer = bottom + list(queue)
for i in answer:
    print(i, end=' ')