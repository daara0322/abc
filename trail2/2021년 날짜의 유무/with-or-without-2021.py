M, D = map(int, input().split())

# Please write your code here.

def fun3() :
    if D <= 31 :
        return True
    else:
        return False

def fun4() :
    if M == 2 :
        if D <= 28 :
            return True
    else :
        if D <= 30 :
            return True
        else :
            return False


def fun2():
    if M%2 != 0:
        return fun3()
    else :
        return fun4()


def fun1() :
    if M%2 == 0 :
        return fun3()
    else :
        return fun4()



if M < 8 :
    if fun2() :
        print("Yes")
    else :
        print("No")
elif M >= 8 and M <= 12:
    if fun1() :
        print("Yes")
    else :
        print("No")
else :
    print("No")
    
