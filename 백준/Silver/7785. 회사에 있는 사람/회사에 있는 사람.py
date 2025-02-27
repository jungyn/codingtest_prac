n = int(input())
li = set()
for _ in range(n):
    people = input()
    ps = people.split()
    if ps[-1] == 'enter':
        li.add(ps[0])
    elif ps[-1] == 'leave':
        li.remove(ps[0])
# 정렬
li = sorted(li)[::-1]
for i in li:
    print(i) 