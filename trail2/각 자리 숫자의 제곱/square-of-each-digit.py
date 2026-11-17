N = int(input())

# Please write your code here.

def fun(n):
    if n < 10 :
        return n**2
    
    return fun(n//10) + (n%10)**2

print(fun(N))