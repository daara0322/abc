a, b = map(int, input().split())

# Please write your code here.

def fun(x, y):
    if x > y :
        x *= 2 
        y += 10
    else :
        x += 10
        y *= 2

    return x, y

a, b = fun(a, b)
print(a, b)