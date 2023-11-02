def solution(box, n):
    answer = 0
    b0 = box[0] // n  
    b1 = box[1] // n 
    b2 = box[2] // n
    answer = b0 * b1 * b2
    return answer