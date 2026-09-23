n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
OFFSET = 10000
a = OFFSET 
lineC = [""] * 20000

for i in range(n):
    if dir[i] == 'R' :
        for j in range(a, a+x[i]) :
            lineC[j] = "B"
        a += x[i] - 1 
    else :
        for j in range(a, a-x[i], -1) :
            lineC[j] = "W"
        a -= x[i] -1

w, b = 0, 0
for i in range(len(lineC)) :
    if lineC[i] == "B" :
        b += 1
    elif lineC[i] == "W" :
        w += 1

print(w, b)