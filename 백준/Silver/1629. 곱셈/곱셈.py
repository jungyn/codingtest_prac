# 분할정복
a, b, c = map(int, input().split())

def divide(base, power, div):
    if power == 1:
        return base % div
    elif power % 2 == 0:
        temp = divide(base, power // 2, div)
        return (temp * temp) % div 
    else:
        temp = divide(base, power // 2, div)
        return (temp * divide(base, power // 2 + 1, div) % div)

print(divide(a, b, c))