T = int(input())
for test_case in range(1, T + 1):
	num = list(map(int, input().split()))
	answer=max(num)
	print('#{} {}'.format(test_case, answer))