num = int(input())
arr = []
for n in range(1, num+1):
    if n%2 == 0:
        continue
    elif n%3 == 0:
        continue
    elif n%5 == 0:
        continue
    else :
        arr.append(n)

print(len(arr))