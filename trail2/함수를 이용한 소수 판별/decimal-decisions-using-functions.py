a, b = map(int, input().split())

# Please write your code here.
cnt = 0 
bo_val = True 

def fun(n) :
    for i in range(2, n):
        if n%i == 0 :
            return True
    return False

sum_val = 0

for i in range(a, b+1) :
    if fun(i) == False :
        sum_val += i

print(sum_val)



    