T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    if n < 3:
        answer = 0
    else:
        answer = n // 3
        
    print('#{} {}'.format(test_case, answer))
