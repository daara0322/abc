st1 = input()
st2 = input()
st1_sum = ''
st2_sum = ''

for elem in st1 :
    if elem >= '0' and elem <= '9':
        st1_sum += elem 

for elem in st2 :
    if elem >= '0' and elem <= '9':
        st2_sum += elem

print(int(st1_sum) + int(st2_sum))
