a, b, c = map(int, input().split())
if b == c:
    print(-1)
else:
    answer = a // (c-b) + 1
    if answer < 0:
        print(-1)
    else:
        print(answer)