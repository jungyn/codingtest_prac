# 유클리드 호제법
a, b = map(int, input().split())

def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

print(gcd(a, b))
print(a*b//gcd(a,b))