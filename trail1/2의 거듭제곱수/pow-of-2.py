n = int(input())
sum_val = 0

while True :
    if n == 1 :
        break
    else :
        n = n//2 
        sum_val += 1

print(sum_val)