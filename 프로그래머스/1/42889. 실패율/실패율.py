def solution(N, stages):
    answer = []
    bm = []
    bj = []
    temp = []
    ratio = []
    
    for i in range(1, N+1):
        bj.append(stages.count(i))
        bm.append(len(stages))
    
    for j in range(len(bj)):
        t = bm[j] - sum(bj[:j+1])
        temp.append(t)
        
    for k in range(1, N):
        bm[k] = temp[k-1]
        
    for x in range(N):
        if bm[x] == 0:
            ratio.append(0)
        else:
            ratio.append(bj[x] / bm[x])

    answer = [idx+1 for idx,val in sorted(enumerate(ratio), key=lambda x : x[1], reverse=True)]

    return answer