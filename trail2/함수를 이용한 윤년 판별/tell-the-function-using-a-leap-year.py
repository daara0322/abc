y = int(input())

# Please write your code here.
def fun(n):
    if n % 4 != 0 :
        return False
    if n % 100 == 0 and n % 400 != 0 :
        return False
    
    return True

if fun(y) == True :
    print('true')
else :
    print('false')