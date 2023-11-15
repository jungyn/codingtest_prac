T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    num = [2, 3, 5, 7, 11]
    count = [0, 0, 0, 0, 0]
    for i in range(5):
        while N % num[i] == 0:
            count[i] += 1
            N //= num[i]
        
    print(f'#{test_case}', *count)