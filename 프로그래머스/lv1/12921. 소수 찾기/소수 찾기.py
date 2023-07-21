def solution(n):
    # 에라토스테네스 체
    num=set(range(2,n+1))
    for i in range(2,n+1):
        if i in num:          # 만약 i가 num 집합에 있다면
            num -= set(range(2*i,n+1,i)) # i의 배수는 num 집합에서 제외
    return len(num)