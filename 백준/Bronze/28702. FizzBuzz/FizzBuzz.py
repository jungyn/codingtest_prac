p1 = input()
p2 = input()
p3 = input()

su = 0

if p1.isdigit():
    su = int(p1) + 3
elif p2.isdigit():
    su = int(p2) + 2
elif p3.isdigit():
    su = int(p3) + 1

if su % 3 == 0 and su % 5 == 0:
    print('FizzBuzz')
elif su % 3 == 0:
    print('Fizz')
elif su % 5 == 0:
    print('Buzz')
else:
    print(su)