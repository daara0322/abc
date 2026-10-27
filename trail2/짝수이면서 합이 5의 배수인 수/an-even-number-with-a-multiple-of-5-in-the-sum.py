n = int(input())

# Please write your code here.

def fun(n):
    st = str(n)
    stn = int(st[0]) + int(st[1])
    if n%2 == 0 and stn % 5 == 0 :
        return True
    else :
        return False

if fun(n) == True :
    print("Yes")
else :
    print("No")
