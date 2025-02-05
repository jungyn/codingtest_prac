n, m = map(int, input().split())
su = list(map(int, input().split()))
answer = 0

left = 0
current_sum = 0

for right in range(n):
    current_sum += su[right]

    while current_sum > m:
        current_sum -= su[left]
        left += 1

    if current_sum == m:
        answer += 1
        
print(answer)