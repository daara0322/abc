n = int(input())

# Please write your code here.

def fun(n) :
    if n == 0 :
        return 
    fun(n-1)
    print(n, end=' ')

def fun1(n):
    if n == 0:
        return
    print(n, end=' ')
    fun1(n-1)

fun(n)
print()
fun1(n)