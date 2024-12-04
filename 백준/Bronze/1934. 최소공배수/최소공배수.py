T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    
    # 최소공약수
    def gcd(a, b):
        while b%a != 0:
            a, b = b%a, a
        return a

    # 최대공배수
    def lcm(a, b):
        return a*b // gcd(a,b)
        
    print(lcm(a,b))