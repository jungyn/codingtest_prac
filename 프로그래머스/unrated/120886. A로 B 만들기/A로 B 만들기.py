def solution(before, after):
    bef_list = []
    aft_list = []
    
    for i in before:
        bef_list.append(i)
    bef_list.sort()
    
    for j in after:
        aft_list.append(j)
    aft_list.sort()
    
    if bef_list == aft_list:
        answer = 1
    else:
        answer = 0
    return answer