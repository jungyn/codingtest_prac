h, m = map(int, input().split())

if h == 0 and m < 45:
    print(23, 60-45+m)

elif m >= 45:
    print(h, m-45)

else:
    print(h-1, 60-45+m)