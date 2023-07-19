def solution(nums):
    answer = 0
    ev = int(len(nums) / 2)
    nums = set(nums)
    answer = min(len(nums), ev)
    
    return answer