def solution(i, j, k):
    answer = 0
    
    for x in range(i, j+1):
        if str(x).find(str(k)) != -1:
            answer += int(str(x).count(str(k)))
    return answer