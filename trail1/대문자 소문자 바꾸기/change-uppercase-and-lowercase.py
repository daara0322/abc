a = input()

for elem in a :
    if elem >= 'a' and elem <= 'z' :
        print(elem.upper(), end="")
    else :
        print(elem.lower(), end ='')