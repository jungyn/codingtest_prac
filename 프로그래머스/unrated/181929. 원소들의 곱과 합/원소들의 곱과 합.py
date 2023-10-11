def solution(num_list):
    pro = 1
    sum = 0
    
    for i in range(len(num_list)):
        pro *= num_list[i]
        sum += num_list[i]
        
    if pro < sum**2:
        return 1
    else:
        return 0
        