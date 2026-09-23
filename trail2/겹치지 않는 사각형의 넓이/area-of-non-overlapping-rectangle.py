x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
answer = 0

for i in range(2):
    area = (x2[i] - x1[i]) * (y2[i] - y1[i])

    width = max(0, min(x2[i], x2[2]) - max(x1[i], x1[2]))
    height = max(0, min(y2[i], y2[2]) - max(y1[i], y1[2]))

    answer += area - width * height

print(answer)