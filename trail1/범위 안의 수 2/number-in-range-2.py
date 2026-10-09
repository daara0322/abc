sum_val = 0
avg_len = 0

for _ in range(10):
    a = int(input())
    if a >= 0 and a <=200 :
        sum_val+=a
        avg_len+=1
    
print(sum_val,end=" ")
print(f"{sum_val/avg_len:.1f}")