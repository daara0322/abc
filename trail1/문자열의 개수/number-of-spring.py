cnt = 0 
arr_st = []
for i in range(200) :
    st = input()
    if st == '0' :
        break
    cnt+=1
    if cnt % 2 == 1 :
        arr_st.append(st)

print(cnt)

for elem in arr_st :
    for j in elem :
        print(j, end='')
    print()

