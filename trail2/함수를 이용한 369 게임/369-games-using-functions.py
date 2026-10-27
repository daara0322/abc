a, b = map(int, input().split())

# Please write your code here.
def fun2(x) : 
    if x % 3 == 0:
        return True

def fun3(x) :
    if ('3' in str(x)) or ('6' in str(x)) or ('9' in str(x)):
        return True 

def fun1(x) :
    if fun3(x) or (fun2(x)):
        return True 

cnt = 0
for i in range(a, b+1):
    if fun1(i) == True :
        cnt+=1

print(cnt)