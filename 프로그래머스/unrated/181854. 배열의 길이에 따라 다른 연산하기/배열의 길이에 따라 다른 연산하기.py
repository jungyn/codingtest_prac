def solution(arr, n):
    answer = []
    for idx, val in enumerate(arr):
        if len(arr) % 2 != 0:
            if idx % 2 == 0:
                val += n
            answer.append(val)
        else:
            if idx % 2 != 0:
                val += n
            answer.append(val)
    return answer