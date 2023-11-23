T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    li = list(map(int, input().split()))
    
    avg = sum(li) / n
    
    count = 0
    for i in li:
	    if i <= avg:
        	count += 1
    print('#{} {}'.format(test_case, count))