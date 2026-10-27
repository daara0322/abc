n = int(input())

# Please write your code here.
def fun(n):
    sum_val = 0
    for i in range(1, n+1):
        sum_val += i
    return sum_val // 10

def fun2(n):
    print(n)

fun_val = fun(n)
fun2(fun_val)