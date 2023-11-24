T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    
    print('#{}'.format(test_case), end=' ')
    for i in range(n):
        print(x[i], end=' ')
    print()