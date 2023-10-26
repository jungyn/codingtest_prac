def solution(myString, pat):
    answer = 0
    myString = myString.replace("A", "C")
    myString = myString.replace("B", "D")
    
    pat = pat.replace("A", "D")
    pat = pat.replace("B", "C")
    
    if pat in myString:
        answer = 1
    else:
        answer = 0
        
    return answer