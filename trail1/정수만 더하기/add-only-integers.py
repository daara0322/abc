A = input()
sum_val = 0
for elem in A :
    if (elem >= 'a' and elem <= 'z') or (elem >= 'A' and elem <= 'Z'):
        continue
    else :
        sum_val += int(elem)

print(sum_val)