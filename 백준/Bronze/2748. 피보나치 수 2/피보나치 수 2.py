# 재귀함수 X
n = int(input())
fibol = []

def fibo(x):
    for i in range(x+1):
        if i == 0:
            num = 0
        elif i == 1 or i == 2:
            num = 1
        else:
            num = fibol[-1] + fibol[-2]
        fibol.append(num)

fibo(n)
print(fibol[-1])