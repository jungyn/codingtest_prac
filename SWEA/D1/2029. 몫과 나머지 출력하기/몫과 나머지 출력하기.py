T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    quo = a // b
    rem = a % b
    print('#{} {} {}'.format(test_case, quo, rem))