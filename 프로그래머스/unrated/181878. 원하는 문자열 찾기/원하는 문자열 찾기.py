def solution(myString, pat):
    answer = 0
    myString = myString.upper()
    pat = pat.upper()
    if myString.find(pat) >= 0:
        answer = 1
    return answer