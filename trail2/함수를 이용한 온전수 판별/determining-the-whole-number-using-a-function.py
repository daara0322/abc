a, b = map(int, input().split())

# Please write your code here.

def fun3(n):
    if n%3 == 0 and n%9 != 0 :
        return False


def fun2(n):
    if n % 10 == 5 :
        return False

def fun1(n) :
    if n%2 == 0 :
        return False
    elif fun2(n) == False :
        return False
    elif fun3(n) == False :
        return False
    else :
        return True

cnt = 0
for i in range(a, b+1):
    if fun1(i) == True :
        cnt += 1
    
print(cnt)