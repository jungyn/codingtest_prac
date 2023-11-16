T = int(input())
for test_case in range(1, T + 1):
    p, q, r, s, w = map(int, input().split())
    
    a = p*w
    b=q
    if r < w:
        b += s * (w-r)
    cost = min(a,b)
    
    print('#{} {}'.format(test_case, cost))