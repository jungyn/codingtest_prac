def solution(my_string, s, e):
    answer = ''
    mid = my_string[s:e+1]
    return my_string[:s] + mid[::-1] + my_string[e+1:]