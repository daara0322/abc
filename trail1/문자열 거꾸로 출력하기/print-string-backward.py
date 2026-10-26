for _ in range (10) :
    st = input()
    if st == 'END' :
        break
    else :
        for i in range(len(st)):
            print(st[len(st)-1-i], end='')
        print()