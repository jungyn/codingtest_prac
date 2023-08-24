def solution(num_list):
    answer = []
    odd, even = 0, 0
    for num in num_list:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
            
    answer = [even, odd]
    return answer