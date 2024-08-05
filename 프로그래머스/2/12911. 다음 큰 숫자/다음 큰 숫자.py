def solution(n):
    answer = 0
    two = bin(n)[2:]
    two_c = two.count('1')
    
    for i in range(n+1, 2*n):
        if bin(i)[2:].count('1') == two_c:
            answer += int(i)
            break
    return answer