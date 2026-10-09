cnt3 = 0
cnt5 = 0 

for _ in range(10):
    a = int(input())
    if a % 3 == 0 and a % 5 == 0:
        cnt3 += 1
        cnt5 += 1
    elif a % 3 == 0 :
        cnt3 += 1
    elif a % 5 == 0 :
        cnt5 += 1

print(cnt3, end=' ')    
print(cnt5, end=' ')