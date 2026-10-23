st = input()
string =''
arr = list(st)
c = st[1]
for i in range(len(st)):
    if st[i] == c :
        arr[i] = arr[0]

print(''.join(arr))

