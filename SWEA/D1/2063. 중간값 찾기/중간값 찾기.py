N = int(input())
num = list(map(int, input().split()))
num.sort()
answer = num[N//2]
print(answer)