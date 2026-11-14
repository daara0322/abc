A = input()

# Please write your code here.

def fun(x):
    leng = len(x) 
    for i in range(leng):
        if x[i] != x[0]:
            return True
    return False
    
if fun(A) :
    print('Yes')
else:
    print('No')


