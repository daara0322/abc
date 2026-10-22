st = input()
n = int(input())

if n > len(st) :
    for i in range(len(st)-1, -1, -1):
        print(st[i], end="")
else:
    for i in range(len(st)-1, len(st)-n-1, -1):  
        print(st[i], end="")