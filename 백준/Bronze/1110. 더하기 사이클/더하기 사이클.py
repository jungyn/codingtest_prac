n = int(input())
cheak = n
answer = 0

while True:
    hap = n//10 + n%10
    new = n%10*10 + hap%10
    answer += 1
    n = new
    if new == cheak:
        break

print(answer)