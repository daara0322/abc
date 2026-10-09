n = int(input())
cnt2 = 0
cnt3 = 0
cnt12 = 0

for i in range(n+1) :
    if i == 0 :
        continue
    elif i % 2 == 0 :
        if i % 3 == 0:     
            if i % 12 == 0:
                cnt12 += 1
            else :
                cnt3 += 1
        else :
            cnt2 += 1
    elif i % 3 == 0 :
        if i % 12 == 0:
            cnt12 += 1
        else :
            cnt3 += 1
    elif i % 12 == 0:
        cnt12+= 1

print(cnt2, end=' ')
print(cnt3, end=' ')
print(cnt12, end=' ')