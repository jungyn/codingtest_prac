def solution(array):
    answer = 0
    for i in str(array):
        answer += i.count('7')
    return answer