n = int(input())
switch = [-1] + list(map(int, input().split()))
students = int(input())
for _ in range(students):
    sex, num = map(int, input().split())
    if sex == 1:
        for i in range(num, len(switch), num):
            if switch[i] == 0:
                switch[i] = 1
            else:
                switch[i] = 0
    elif sex == 2:
        if switch[num] == 0:
            switch[num] = 1
        else:
            switch[num] = 0
        
        i = 1
        while num - i >= 1 and num + i <= n and switch[num-i] == switch[num+i]:
            switch[num-i] = 1 if switch[num-i] == 0 else 0
            switch[num+i] = 1 if switch[num+i] == 0 else 0
            i += 1
            
for li in range(1, len(switch)):
    print(switch[li], end=" ")
    if li % 20 == 0:
        print()