st = input()

for i in range(len(st)-1, -1, -1):
    if i %2 != 0 :
        print(st[i], end="")