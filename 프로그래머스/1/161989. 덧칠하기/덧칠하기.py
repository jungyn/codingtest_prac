def solution(n, m, section):
    answer = 0
    paint = [1] * n
    for i in section:
        paint[i-1] = 0
    
    cur = 0   # 현재 위치
    while cur < n:
        if paint[cur] == 0:
            answer += 1
            for j in range(cur, min(cur+m, n)):
                paint[j] = 1
            cur += m
        else:
            cur += 1
    return answer