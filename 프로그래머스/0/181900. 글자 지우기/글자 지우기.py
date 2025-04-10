def solution(my_string, indices):
    answer = ''
    lst = []
    for i in range(len(my_string)):
        lst.append(i)
    for j in indices:
        lst.remove(j)
    for k in lst:
        answer += my_string[k]
    return answer