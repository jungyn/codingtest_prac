def solution(numer1, denom1, numer2, denom2):
    bm = denom1 * denom2
    bj = numer1*denom2 + numer2*denom1
    
    # 최대공약수
    start = max(bm, bj)
    gcd = 1
    
    for i in range(start, 0, -1):
        if bm % i == 0 and bj % i == 0:
            gcd = i
            break
            
    answer = [bj/gcd, bm/gcd]       
    return answer