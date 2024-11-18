n = int(input())

count = 0
endNum = 666

while True:
    if '666' in str(endNum):
        count += 1
    if count == n:
        break
    else:
        endNum += 1
print(endNum)