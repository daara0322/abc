st = input()
for _ in range(len(st)):
    if len(st) == 1 :
        break

    n = int(input())
    if len(st) <= n :
        st = st[:len(st)-1]
        print(st)
    else :
        st = st[:n] + st[n+1:]
        print(st)

