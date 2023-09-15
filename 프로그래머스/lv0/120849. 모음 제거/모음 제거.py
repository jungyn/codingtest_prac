def solution(my_string):
    moem = ['a', 'e', 'i', 'o', 'u']
    
    for i in moem:
        if i in my_string:
            my_string = my_string.replace(i, '')
    return my_string