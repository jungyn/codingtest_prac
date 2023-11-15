def solution(n):
    answer = 0
    for i in range(1, 11):
        pass
        fac = 1
        for j in range(1, i+1):
            fac *= j
        
        if fac > n:
                break
        answer = i
    return answer