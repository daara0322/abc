n = int(input())
st = True

for i in range(2, n):
    if n%i == 0 :
        st = False
    
if st == True :
    print("P")
else :
    print("C")
