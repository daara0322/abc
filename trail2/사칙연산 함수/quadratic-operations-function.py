a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.

def add(a, c) :
    return a+c

def mn(a, c) :
    return a-c
def sq(a, c):
    return a*c

def sp(a, c):
    return a//c

if o == '+' :
    print(f"{a} {o} {c} = {add(a, c)}")
elif o == '-':
    print(f"{a} {o} {c} = {mn(a, c)}")
elif o == '/' :
    print(f"{a} {o} {c} = {sp(a, c)}")
elif o == '*' :
    print(f"{a} {o} {c} = {sq(a,c)}")
else :
    print(False)