T = int(input())
for _ in range(T):
    h, w, n = map(int, input().split())
    if n % h == 0:
        room = n // h
        floor = h
    else:
        room = n // h + 1
        floor = n % h

    print(f"{floor}{room:02d}")