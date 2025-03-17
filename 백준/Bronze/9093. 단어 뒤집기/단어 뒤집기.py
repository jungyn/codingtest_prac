T = int(input())
for _ in range(T):
    sent = input()
    sent_spl = sent.split()
    rep = []
    for i in sent_spl:
        rep.append(i[::-1])
    print(' '.join(rep))