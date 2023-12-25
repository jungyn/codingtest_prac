def solution(a, b):
    answer = 0
    o_plus = int(str(a) + str(b))
    t_mul = 2 * a * b
    answer = max(o_plus, t_mul)
    return answer