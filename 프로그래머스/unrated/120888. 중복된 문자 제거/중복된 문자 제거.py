def solution(my_string):
    answer = ''
    for i, val in enumerate(my_string):
        if i == my_string.index(val):
            answer += val
    return answer