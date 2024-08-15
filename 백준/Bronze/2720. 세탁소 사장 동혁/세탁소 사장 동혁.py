T = int(input())
for _ in range(T):
    money = int(input())
    
    c = [25, 10, 5, 1]
    for i in c:
        print(money // i, end = ' ')
        money = money % i