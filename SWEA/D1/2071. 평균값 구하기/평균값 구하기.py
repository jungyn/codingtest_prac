T = int(input())

for test_case in range(1, T + 1):
    a, b, c, d, e, f, g, h, i, j = map(int, input().split())
    sum = a + b + c + d + e + f + g + h + i + j
    avg = sum / 10
    answer = int(round(avg, 0))

    print('#{} {}'.format(test_case, answer))
