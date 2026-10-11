sf = [False, False, False, False, False]
for i in range(5):
    n = int(input())
    if n%3==0 :
        sf[i] = True
    
if False in sf :
    print(0)
else :
    print(1)
    