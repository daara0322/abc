n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def fun(n) :
    if n == 0 :
        return arr[0]
    
    return max(arr[n-1], fun(n-1))

print(fun(n))
    

