def solution(X, Y):
    answer = ''
    x_list = [X.count(str(i)) for i in range(10)]
    y_list = [Y.count(str(i)) for i in range(10)]
    
    for i in range(9,-1,-1):
        for _ in range(min(x_list[i], y_list[i])):
            answer += str(i)
            
    if answer == "":
        answer = '-1'
    elif answer[0] == '0':
        answer = '0'
    return answer