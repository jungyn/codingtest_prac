def solution(n, lost, reserve):
    answer = 0
    dp = [1] * (n+2)
    dp[0], dp[-1] = -1, -1
    for i in reserve:
        dp[i] += 1
    for j in lost:
        dp[j] -= 1
    # print(dp)
        
    for k in range(1, n+1):
        if (dp[k] == 2 and dp[k-1] == 0):
            dp[k], dp[k-1] = 1, 1
        if (dp[k] == 2 and dp[k+1] == 0):
            dp[k], dp[k+1] = 1, 1
    
    dp = dp[1:n+1]
    for d in dp:
        if d >= 1:
            answer += 1
    return answer