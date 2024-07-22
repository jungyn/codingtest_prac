# 소수 판별 함수
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    su = []
    
    # 3개의 합 리스트에 넣기
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                su.append(nums[i]+nums[j]+nums[k])
    su.sort()
    
    # 소수 구하기
    for s in su:
        if is_prime(s):
            answer += 1
    return answer