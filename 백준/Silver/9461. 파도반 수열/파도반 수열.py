T = int(input())

for _ in range(T):
    n = int(input())
    dp = [1] * (n+1)
    for i in range(4, n+1):
        dp[i] = dp[i-2] + dp[i-3]
    print(dp[-1
             ])