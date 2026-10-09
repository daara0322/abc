a, b = map(int, input().split())
sum_val = 0
sum_len = 0
for i in range(a, b+1) :
    if i % 5 == 0 or i % 7 == 0:
        sum_val += i 
        sum_len += 1

avg = sum_val/sum_len
print(sum_val, end=' ')
print(f"{avg:.1f}")