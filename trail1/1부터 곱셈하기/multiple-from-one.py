n = int(input())
pond = 1
for i in range(1, 11):
    pond *= i
    if pond >= n :
        a = i
        break
print(a)