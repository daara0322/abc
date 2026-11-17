n = int(input())

# Please write your code here.

def fun1(n):
    if n == 0:
        return 
    fun1(n-1)
    print('*'*n)

fun1(n)