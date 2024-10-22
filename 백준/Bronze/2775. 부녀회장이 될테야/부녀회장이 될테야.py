T = int(input())
for _ in range(T):
    floor = int(input()) # 층
    num = int(input()) # 호
    people = [i for i in range(1, num+1)] # 0층

    for k in range(floor):
        new = []
        for n in range(num):
            new.append(sum(people[:n+1]))
        people = new.copy()
    print(new[-1])