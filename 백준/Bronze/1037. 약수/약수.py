n = int(input())
nums = map(int, input().split())

nums = sorted(nums)
print(nums[0] * nums[-1])