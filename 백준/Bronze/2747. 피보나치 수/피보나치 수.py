n = int(input())
fibo_list = []

def fibo(x):
    for i in range(x+1):
        if i == 0:
            num = 0
        elif i == 1:
            num = 1
        else:
            num = fibo_list[-1] + fibo_list[-2]
        fibo_list.append(num)

fibo(n)
print(fibo_list[-1])