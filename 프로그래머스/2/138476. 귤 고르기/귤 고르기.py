def solution(k, tangerine):
    answer = 1
    count = {}
    cum = 0
    for i in tangerine:
        try:
            count[i] += 1
        except:
            count[i] = 1
    sort_cnt = sorted(count.items(), key=lambda x:x[1], reverse=True)
    for j in sort_cnt:
        cum += j[1]
        if cum < k:
            answer += 1
    return answer