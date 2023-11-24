T = int(input())

for test_case in range(1, T + 1):
    word = input()
    result = ''
    for i in range(len(word)):
        if word[i] in ['a', 'e', 'i', 'o', 'u']:
            continue
        result += word[i]
    print('#{} {}'.format(test_case, result))