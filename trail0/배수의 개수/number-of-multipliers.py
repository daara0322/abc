arr = []
cnt=0
cnt1=0
for j in range(10):
    arr.append(int(input())) 

for i in arr:
    if i % 15 ==0:
        cnt+=1
        cnt1+=1
    elif i % 3 ==0:
        cnt+=1
    elif i % 5 ==0:
        cnt1+=1

print(cnt, cnt1)