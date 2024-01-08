def solution(polynomial):
    x_num = 0
    num = 0
    
    polynomial = polynomial.replace(' ', '').split('+')
    for i in polynomial:
        if i.isdigit():
            num += int(i)
        else:
            if i == 'x':
                x_num += 1
            else:
                x_num += int(i[:-1])
                
    if x_num == 1:
        if num > 0:
            return f'x + {num}'
        else:
            return f'x'
        
    elif x_num > 1:
        if num > 0:
            return f'{x_num}x + {num}'
        else:
            return f'{x_num}x'
    else:
        return f'{num}'