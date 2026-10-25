st = input()

for elem in st:
    if ('A' <= elem and 'Z' >= elem) or ('a' <= elem and 'z' >= elem):
        print(elem.lower(), end='')
    elif ord(elem) >= 48 and ord(elem) <= 57 :
        print(elem, end='') 
    