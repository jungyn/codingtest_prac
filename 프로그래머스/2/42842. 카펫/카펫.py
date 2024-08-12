def solution(brown, yellow):
    answer = []
    
    value = brown + yellow
    for i in range(1, int(value**0.5 + 1)):
        if value % i == 0:
            if (value//i * 2) + ((i-2) * 2) == brown:
                answer += value//i, i
    return answer