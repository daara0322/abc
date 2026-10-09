sum_val = 0
arr = []
while True :
    a = int(input())
    if a % 2 == 0 :
        print(a//2)
        sum_val += 1
    else :
        continue
    if sum_val == 3 :
        break
