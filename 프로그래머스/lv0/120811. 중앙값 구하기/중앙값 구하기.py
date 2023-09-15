def solution(array):
    array.sort()
    if len(array) % 2 == 1:
        answer = array[len(array) // 2]
    return answer