N = int(input())

# Please write your code here.

def fun(n):
    if n == 1 :
        return 1 
    
    return n + fun(n-1)

print(fun(N))