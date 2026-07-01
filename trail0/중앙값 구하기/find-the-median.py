a, b, c = map(int, input().split())

if a > b :
    if a > c :
        if b > c :
            print(b)
        else :
            print(c)
    else : 
        print(a)
elif a < b :
    if a > c :
        print(a)
    elif a < c :
        if b < c :
            print(b)
        else : 
            print(c)