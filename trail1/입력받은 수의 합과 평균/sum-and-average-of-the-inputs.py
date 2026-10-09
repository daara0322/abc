n = int(input())
sum_val = 0
avg_len = 0
for _ in range(n):
    a = int(input())
    sum_val += a
    avg_len += 1

print(sum_val, end=' ')
print(f"{sum_val/avg_len:.1f}")