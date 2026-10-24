st = input()
l = len(st)
print(st)
for i in range(l):
    st = st[-1] + st[:-1]
    print(st) 