arr = []
for _ in range(2) :
    arr.append(list(map(int, input().split())))

suma = 0
sumb = 0
sumc = 0
sumd = 0
sume = 0
sumf = 0
sumg = 0
for i in range(4):
    sumb += arr[0][i]

for i in range(4):
    sumc += arr[1][i]

for i in range(2):
    sumd += arr[i][0]

for i in range(2):
    sume += arr[i][1]

for i in range(2):
    sumf += arr[i][2]

for i in range(2):
    sumg += arr[i][3]

for i in range(2) :
    for j in range(4) :
        suma += arr[i][j]

print(f"{sumb/4:.1f} {sumc/4:.1f}")
print(f"{sumd/2:.1f} {sume/2:.1f} {sumf/2:.1f} {sumg/2:.1f}")
print(f"{suma/8:.1f}")