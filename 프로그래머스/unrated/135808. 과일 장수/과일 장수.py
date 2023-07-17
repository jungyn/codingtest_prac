def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    for i in range(len(score)):
        if i % m == 0:
            if len(score[i:i+m]) == m:
                box = score[i:i+m]
                answer += min(box)*m
    return answer