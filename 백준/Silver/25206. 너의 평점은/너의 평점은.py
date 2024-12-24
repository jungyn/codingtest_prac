answer = 0
sum_score = 0

for _ in range(20):
    name, score, grade = map(str, input().split())

    if grade == 'P':
        pass
    elif grade == 'A+':
        answer += 4.5 * float(score)
        sum_score += float(score)
    elif grade == 'A0':
        answer += 4.0 * float(score)
        sum_score += float(score)
    elif grade == 'B+':
        answer += 3.5 * float(score)
        sum_score += float(score)
    elif grade == 'B0':
        answer += 3.0 * float(score)
        sum_score += float(score)
    elif grade == 'C+':
        answer += 2.5 * float(score)
        sum_score += float(score)
    elif grade == 'C0':
        answer += 2.0 * float(score)
        sum_score += float(score)
    elif grade == 'D+':
        answer += 1.5 * float(score)
        sum_score += float(score)
    elif grade == 'D0':
        answer += 1.0 * float(score)
        sum_score += float(score)
    elif grade == 'F':
        answer += 0.0 * float(score)
        sum_score += float(score)

print(answer / sum_score)