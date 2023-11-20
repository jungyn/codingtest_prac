def solution(array, n):
    array.sort()
    answer = 0
    comp = n + 100
    
    for i in array:
        if abs(i-n) < comp:
            comp = abs(i-n)
            answer = i
    return answer