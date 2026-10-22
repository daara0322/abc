st1 = input()
st2 = input()
st3 = input()

a = len(st1)
b = len(st2)
c = len(st3)

arr = []
arr.append(a)
arr.append(b)
arr.append(c)

print(max(arr)-min(arr))