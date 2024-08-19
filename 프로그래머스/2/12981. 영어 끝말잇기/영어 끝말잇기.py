def solution(n, words):
    answer = []
    number, order = 0, 0
    used_words = []
    
    used_words.append(words[0])
    last_words = words[0][-1]
    
    for i in range(1, len(words)):
        if words[i] not in used_words and last_words == words[i][0]:
            used_words.append(words[i])
            last_words = words[i][-1]
        else:
            number = i%n+1
            order = i//n+1
            break

    return [number, order]