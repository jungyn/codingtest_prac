n = int(input())
dp = [0] * (n+1)
stairs = [0] * (n+1)

for i in range(1,n+1):
    stairs[i] = int(input())

    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

print(dp[-1])