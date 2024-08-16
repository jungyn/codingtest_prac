i = 0
while True:
    L, P, V = map(int, input().split())

    if L == 0 and P == 0 and V == 0:
        break
    else:
        answer = V // P * L + min(V % P, L)
        i += 1
        print("Case {}:".format(i), answer)