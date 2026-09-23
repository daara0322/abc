n = int(input())

commands = [tuple(input().split()) for _ in range(n)]

OFFSET = 100000

linec = [""] * 200001

a = OFFSET

for x1, x2 in commands:
    x1 = int(x1)

    if x2 == 'R':
        for i in range(a, a + x1):
            linec[i] += 'B'

        a += x1 - 1

    else:
        for i in range(a, a - x1, -1):
            linec[i] += 'W'

        a -= x1 - 1

w, b, g = 0, 0, 0

for i in range(len(linec)):
    if linec[i].count('B') >= 2 and linec[i].count('W') >= 2:
        g += 1
    elif linec[i].endswith('B'):
        b += 1
    elif linec[i].endswith('W'):
        w += 1

print(w, b, g)