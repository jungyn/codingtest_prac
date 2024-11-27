a = int(input())
b = int(input())

three = a*(b%10)
four = a*((b%100)//10)
five = a*(b//100)

print(three)
print(four)
print(five)
print(three+four*10+five*100)