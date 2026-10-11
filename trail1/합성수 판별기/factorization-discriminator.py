n = int(input())
sf = False

for i in range(2, n):
    if n%i == 0 :
        sf = True

if sf == True :
    print("C")
else :
    print("N")