N = int(input())
arr = [2, 4]
# Please write your code here.

def fun(n) :
    for i in range(2, n):
        arr.append((arr[i-2]*arr[i-1])%100)
    return arr[n-1]

print(fun(N))



