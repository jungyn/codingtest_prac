T = int(input())

for test_case in range(1, T + 1):
    word = input()
    answer = 0
    if word == word[::-1]:
        answer = 1
    print('#{} {}'.format(test_case, answer))