import sys

m = int(input())
s = set()
for _ in range(m):
    cal = sys.stdin.readline().strip()
    if 'add' in cal:
        s.add(int(cal[4:]))
    elif 'remove' in cal:
        s.discard(int(cal[7:]))
    elif 'check' in cal:
        if int(cal[6:]) in s:
            print(1)
        else:
            print(0)
    elif 'toggle' in cal:
        if int(cal[7:]) in s:
            s.discard(int(cal[7:]))
        else:
            s.add(int(cal[7:]))
    elif cal == 'all':
        s = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    elif cal == 'empty':
        s = set()