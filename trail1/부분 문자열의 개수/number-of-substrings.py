A = input()
B = input()
cnt = 0
Alen = len(A)

for i in range(Alen-1):
    if A[i] + A[i+1] == B :
        cnt+=1 

print(cnt)