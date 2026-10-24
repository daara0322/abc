st = input()
idx = -1 

for i in range(len(st)):
    if st[i] == 'e' :
        idx = i
        break

print(st[:idx] + st[idx+1:])