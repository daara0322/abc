str = ["apple", "banana", "grape", "blueberry", "orange"]
a = input()
cnt = 0

for new in str:
    if new[2] == a or new[3] == a :
        print(new)
        cnt += 1

print(cnt)
    