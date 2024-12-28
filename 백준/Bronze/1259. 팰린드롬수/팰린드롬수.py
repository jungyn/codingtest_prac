while True:
    word = input()
    if word == '0':
        break
    else:
        half = len(word) // 2
        if len(word) % 2 != 0:
            if word[:half] == word[half+1:][::-1]:
                print('yes')
            else:
                print('no')
        else:
            if word[:half] == word[half:][::-1]:
                print('yes')
            else:
                print('no')