T = int(input())

for test_case in range(1, T + 1):
    li = list(map(int, input().split()))
    li.sort()
    avg = int(round(sum(li[1:9]) / 8, 0))
    print('#{} {}'.format(test_case, avg))