n = int(input())
sum_avg = 0
for i in range(1, n+1):
    if i % 2 == 0 :
        continue
    elif i % 3 == 0 or i % 5 == 0:
        continue 
    else :
        sum_avg += 1
print(sum_avg)

