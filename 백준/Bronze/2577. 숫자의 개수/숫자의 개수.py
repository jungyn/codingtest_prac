a = int(input())
b = int(input())
c = int(input())

slist = []
su = list('0123456789')
mul = a*b*c
mul = str(mul)
for i in mul:
    slist.append(i)
print(slist.count('0'))
print(slist.count('1'))
print(slist.count('2'))
print(slist.count('3'))
print(slist.count('4'))
print(slist.count('5'))
print(slist.count('6'))
print(slist.count('7'))
print(slist.count('8'))
print(slist.count('9'))