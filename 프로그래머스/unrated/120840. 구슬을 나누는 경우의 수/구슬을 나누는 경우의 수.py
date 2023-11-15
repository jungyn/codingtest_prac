def solution(balls, share):
    answer = 0
    bj_fac = 1
    for i in range(1, balls+1):
        bj_fac *= i
    
    bm_fac1 = 1
    for j in range(1, balls-share+1):
        bm_fac1 *= j
    bm_fac2 = 1
    for k in range(1, share+1):
        bm_fac2 *= k

    bm = bm_fac1 * bm_fac2
    answer = bj_fac / bm
    return answer