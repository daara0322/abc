a, b = map(int, input().split())

# Please write your code here.
def fun2(d) :
    if (d%10 + d//10) % 2 == 0:
        return True
    return False

def fun1(c) :
    for i in range(2, c):
        if c%i == 0:
            return False
    return True


def fun(x, y) :
    cnt = 0
    for i in range(x, y+1):
        if fun1(i) and fun2(i) :
            cnt += 1
    return cnt

print(fun(a, b))