while True:
    n = int(input())
    if n == -1:
        break
    
    yaksu = []
    for i in range(1, n):
        if n % i == 0:
            yaksu.append(i)
    if sum(yaksu) == n:
        print(f"{n} =", " + ".join(map(str, yaksu)))
    else:
        print(n, 'is NOT perfect.')