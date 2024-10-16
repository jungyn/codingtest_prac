def hansu(x):
    cnt = 0
    for i in range(1, x+1):
        nlist = list(map(int, str(i))) # 각 자리수 숫자
        if i < 100:
            cnt +=1
        else:
            if nlist[0] - nlist[1] == nlist[1] - nlist[2]:
                cnt += 1
    return cnt

x = int(input())
print(hansu(x))