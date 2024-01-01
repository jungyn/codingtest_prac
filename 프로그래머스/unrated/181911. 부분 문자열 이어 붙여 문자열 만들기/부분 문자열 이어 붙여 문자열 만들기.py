def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        string = my_strings[i]
        index_s = parts[i][0]
        index_f = parts[i][1]
        answer += string[index_s:index_f+1]
    return answer