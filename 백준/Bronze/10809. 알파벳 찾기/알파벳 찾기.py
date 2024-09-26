s = input()
alpha = list('abcdefghijklmnopqrstuvwxyz')
result = [-1] * len(alpha)

for i,s in enumerate(list(s)):
    idx = alpha.index(s)
    if result[idx] == -1:
        result[idx] = i
print(' '.join(map(str, result)))