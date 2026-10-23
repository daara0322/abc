st = input()
n = len(st)
eexists = False
aexists = False
for i in range(n-1):
    if st[i] + st[i+1] == 'ee':
        eexists = True
    if st[i] + st[i+1] == 'ab' :
        aexists = True

if eexists == True :
    print("Yes", end=" ")
else :
    print("No", end=" ")

if aexists == True :
    print("Yes")
else :
    print("No")