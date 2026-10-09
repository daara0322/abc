a, b = map(int, input().split())
sum_val = 0

if a < b :
    for i in range(a, b+1):
        if i % 5 == 0 :
            sum_val += i
elif a > b:
    for i in range(b, a+1):
        if i%5 == 0:
            sum_val += i
else :
    if a % 5 == 0:
        sum_val += a

print(sum_val) 