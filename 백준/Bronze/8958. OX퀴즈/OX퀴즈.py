n = int(input())
for _ in range(n):
    s = input()
    sp = s.split('X')
    answer = 0
    for i in sp:
        for j in range(1, len(i)+1):
            answer += j
    print(answer)