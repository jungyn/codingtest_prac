import sys
import heapq

input = sys.stdin.readline

n = int(input())
max_heap = []

for i in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(max_heap, -x)
    elif x == 0:
        if len(max_heap) == 0:
            print(0)
        else:
            if max_heap:
                print(-heapq.heappop(max_heap))
            else:
                print(0)