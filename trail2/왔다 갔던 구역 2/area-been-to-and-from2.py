n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.


line = [0] * 2001

a = 0

for i in range(n):
    if dir[i] == 'R':
        for j in range(a, a + x[i]):
            line[j] += 1
        a += x[i]

    else:
        for j in range(a - x[i], a):
            line[j] += 1
        a -= x[i]

cnt = 0

for i in range(len(line)):
    if line[i] >= 2:
        cnt += 1

print(cnt)