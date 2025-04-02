def solution(dartResult):
    score = []
    n = ''
    for i in dartResult:
        if i.isnumeric():
            n += i
        elif i == 'S':
            n = int(n) ** 1
            score.append(n)
            n = ''
        elif i == 'D':
            n = int(n) ** 2
            score.append(n)
            n = ''
        elif i == 'T':
            n = int(n) ** 3
            score.append(n)
            n = ''
        elif i == '*':
            if len(score) == 1:
                score[0] = score[0] * 2
            elif len(score) == 2:
                score[1] = score[1] * 2
                score[0] = score[0] * 2
            elif len(score) == 3:
                score[2] = score[2] * 2
                score[1] = score[1] * 2     
        elif i == '#':
            score[len(score)-1] = score[len(score)-1] * (-1)
    return sum(score)