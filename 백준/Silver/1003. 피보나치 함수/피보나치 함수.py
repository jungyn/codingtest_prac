# 다이나믹 프로그래밍
T = int(input())
d = [(1,0), (0,1)] + [(0,0) for _ in range(50)]

for _ in range(T):
    n = int(input())
    for i in range(2, n+1):
        d[i] = (d[i-1][0] + d[i-2][0], d[i-1][1] + d[i-2][1])
    print(d[n][0], d[n][1])