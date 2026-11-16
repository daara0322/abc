n = int(input())

# Please write your code here.
def f(x):
    if x == 0 :
        return
    f(x-1)
    print("HelloWorld")

f(n)