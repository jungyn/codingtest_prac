n = int(input())

def fact(x):
    ans = 1
    for i in range(1, x+1):
        ans *= i
    return ans

cnt = 0
for i in str(fact(n))[::-1]:
    if i != '0':
        break
    cnt += 1
print(cnt)