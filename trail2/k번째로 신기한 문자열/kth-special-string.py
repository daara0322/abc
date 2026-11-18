n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
str1 = []
bo = True
for elem in str :
    for i in range(len(t)):
        if t[i] == elem[i] :
            bo = True
        else :
            bo = False
            break
    if bo == True :
        str1.append(elem)


str1.sort()
print(str1[k-1])