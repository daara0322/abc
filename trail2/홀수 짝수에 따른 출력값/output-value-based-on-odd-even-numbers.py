N = int(input())

# Please write your code here.

def fun(n):
    if n % 2 == 1 :
        sum_val = 0
        for i in range(1, n+1):
            if i%2 == 1 :
                sum_val += i
        return sum_val
    else :
        sum_val = 0
        for i in range(2, n+1):
            if i%2==0:
                sum_val += i
        return sum_val

print(fun(N))
