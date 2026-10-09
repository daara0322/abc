n = int(input())
sum_val = 0
while True :
    if n == 1 :
        break
    elif n % 2 == 0 :
        n = n//2
        sum_val += 1
    else :
        n = n*3 + 1
        sum_val += 1
    
    
print(sum_val)