n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.



def fun1(x) :
    sum_val = 0
    sum_val += A[x-1]
    while x != 1 :
        if x % 2 == 0 :
            x = x//2
            sum_val += A[x-1]  
        else :
            x = x - 1 
            sum_val += A[x-1]
    return sum_val


print(fun1(m))