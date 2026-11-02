Y, M, D = map(int, input().split())

# Please write your code here.


def fun1() :
    if Y % 4 == 0 and Y % 100 != 0 or (Y%4 == 0 and Y%100 == 0 and Y%400 == 0):
        if D <= 29 :
            return True
        else :
            return False
    else :
        if D <= 28 :
            return True
        else :
            return False

def fun() :
    if M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12 :
        if D <= 31 :
            return True
    elif  M ==4 or M == 6 or M == 9 or M == 11 :
        if D <= 30 :
            return True
    else :
        if fun1() :
            return True 
        else :
            return False

if fun() :
    if M >= 3 and M <= 5 :
        print("Spring")
    elif M >= 6 and M <= 8 :
        print("Summer")
    elif M >= 9 and M <= 11 :
        print("Fall")
    else :
        print("Winter")
else :
    print(-1)