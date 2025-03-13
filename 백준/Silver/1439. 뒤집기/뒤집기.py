s = input()

zero = s.split('0')
one = s.split('1')

z = len(zero) - zero.count('')
o = len(one) - one.count('')

print(min(z, o))