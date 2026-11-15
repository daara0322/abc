text = input()
pattern = input()

# Please write your code here.
def fun(x):
    if x in text :
        a = text.index(x)
        return a 
    else :
        return -1
    

print(fun(pattern))