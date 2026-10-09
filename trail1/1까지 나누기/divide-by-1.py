n = int(input())
sum_avg = 0
i = 0
while n > 1 :
    i += 1
    n = n//i
    sum_avg += 1
    
print(sum_avg)