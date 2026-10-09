n = int(input())
cnt = 0 

for i in range(1, n+1) :
    if i%100 == 0 :
        if i%400 != 0 :
            continue
        else :
            cnt += 1
    elif i%4 == 0:
        cnt+=1

print(cnt)
