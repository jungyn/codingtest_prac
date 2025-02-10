import sys

def my_round(x):
    return int(x) + (1 if x - int(x) >= 0.5 else 0)

input = sys.stdin.readline
n = int(input())
if n == 0:
    print(0)
else:
    cut = my_round(n * 0.15)
    lv = []
    for _ in range(n):
        s = int(input())
        lv.append(s)
    lv.sort()
    lv = lv[cut:n-cut]
    if len(lv) == 0:
        print(0)
    else:
        answer = my_round(sum(lv) / len(lv))
        print(answer)