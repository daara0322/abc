N = int(input())

# Please write your code here.

def fun(n):
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    if n%2 == 0:
        return fun(n-2) + n
    else :
        return fun(n-2) + n
    
print(fun(N))
