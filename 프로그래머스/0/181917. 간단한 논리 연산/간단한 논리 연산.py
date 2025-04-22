def solution(x1, x2, x3, x4):
    if x1 == False and x2 == False:
        cond1 = False
    else:
        cond1 = True
        
    if x3 == False and x4 == False:
        cond2 = False
    else:
        cond2 = True
    
    if cond1 == True and cond2 == True:
        answer = True
    else:
        answer = False
    return answer