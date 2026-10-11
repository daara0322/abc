a, b, c = map(int, input().split())
satisfy = False

for i in range(a, b+1):
    if i%c == 0 :
        satisfy = True

if satisfy == True :
    print("YES")
else :
    print("NO")
    