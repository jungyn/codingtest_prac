def solution(n):
    if n == 1:
        answer = 1
    elif n == 2:
        answer = 2
    else:
        a, b = 1, 2
        for i in range(3, n+1):
            a, b = b, (a+b)
        answer = b
    return answer % 1234567