arr = []

while True :
    a = int(input())
    if a >= 20 and a < 30 :
        arr.append(a)
    else :
        break
b = sum(arr)
c = len(arr)
print(f"{b/c:.2f}")
