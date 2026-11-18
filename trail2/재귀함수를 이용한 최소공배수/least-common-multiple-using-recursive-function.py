from math import gcd
n = int(input())
arr = list(map(int, input().split()))




def fun(n):
    if n == 1:
        return arr[0]
    return (fun(n-1)*arr[n-1])//gcd(fun(n-1), arr[n-1])


print(fun(n))
