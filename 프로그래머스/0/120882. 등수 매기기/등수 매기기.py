def solution(score):
    answer = []
    sub_score = []
    for i in range(len(score)):
        sub_score.append((score[i][0] + score[i][1]) // len(str(i)))
    sort_arr = sorted(sub_score, reverse=True)
    
    for k in sub_score:
        answer.append(sort_arr.index(k)+1)
    return answer