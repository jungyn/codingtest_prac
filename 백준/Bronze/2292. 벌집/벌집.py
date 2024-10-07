room = int(input())
maxbox = 1
answer = 1

while room > maxbox:
    maxbox += 6*answer
    answer += 1
print(answer)