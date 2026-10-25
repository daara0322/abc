st = input()

for elem in st :
    if (ord(elem) >= 97 and ord(elem) <=122) or (ord(elem) >= 65 and ord(elem) <= 90) :
        if ord(elem) >= 65 and ord(elem) <= 90:
            print(elem, end='')
        else :
            print(chr(ord(elem)+ord('A')-ord('a')), end="")