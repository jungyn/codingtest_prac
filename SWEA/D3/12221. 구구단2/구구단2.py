T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    if a >= 10 or b >= 10:
        answer = -1
    else:
        answer = a * b
        
    print('#{} {}'.format(test_case, answer))