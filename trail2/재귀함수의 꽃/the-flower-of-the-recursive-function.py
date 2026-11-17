N = int(input())

# Please write your code here.
def fun(n):
    if n == 0 :
        return
    print(n, end=' ')
    fun(n-1)
    print(n, end=' ')

fun(N)