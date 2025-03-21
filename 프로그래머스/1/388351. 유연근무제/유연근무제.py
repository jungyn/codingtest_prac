def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        hope = schedules[i]
        safe = schedules[i] + 10
        if safe % 100 >= 60:
            safe = safe + 100 - 60
        count = 0
        for j in range(7):
            print('t', timelogs[i][j], startday%7)
            if startday%7 == 6 or startday%7 == 0:
                startday += 1
            else:
                startday += 1
                if timelogs[i][j] <= safe:
                    count += 1
        if count == 5:
            answer += 1
    return answer