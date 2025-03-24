while True:
    a, b, c = map(int, input().split())
    if a > b and a > c:
        if a*a == c*c + b*b:
            print('right')
        else:
            print('wrong')
    elif b > a and b > c:
        if b*b == a*a + c*c:
            print('right')
        else:
            print('wrong')
    elif c > a and c > b:
        if c*c == a*a + b*b:
            print('right')
        else:
            print('wrong')

    if a == 0 and b == 0 and c == 0:
        break
    
