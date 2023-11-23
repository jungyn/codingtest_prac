T = int(input())

for test_case in range(1, T + 1):
    L, U, X = map(int, input().split())
    
    if X >= U:
        answer = -1      
    elif X >= U or X <= L:
        answer = L-X      
    else:
        answer = 0
        
    print('#{} {}'.format(test_case, answer))