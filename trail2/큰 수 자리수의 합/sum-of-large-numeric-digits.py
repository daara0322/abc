a, b, c = map(int, input().split())

# Please write your code here.
def fun(d) :
    if d < 10 :
        return d
    return fun(d//10) + (d%10)
    


d = a*b*c
print(fun(d))