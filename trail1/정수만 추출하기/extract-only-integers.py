st1, st2 = tuple(input().split())
st1_sum = ''
st2_sum = ''

for elem in st1 :
    if elem <= '9' and elem >= '0' :
        st1_sum += elem
    else :
        break

for elem in st2 :
    if elem <= '9' and elem >= '0' :
        st2_sum += elem
    else :
        break

sum_val = int(st1_sum) + int(st2_sum)

print(sum_val)