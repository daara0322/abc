st = input()
cnt1 = 0
cnt2 = 0
n = len(st)

for i in range(n-1):
    if st[i]+st[i+1] == 'ee':
        cnt1 += 1
    if st[i]+st[i+1] == 'eb':
        cnt2 += 1

print(cnt1, cnt2)