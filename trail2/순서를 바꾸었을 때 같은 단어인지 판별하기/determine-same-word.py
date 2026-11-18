word1 = input()
word2 = input()

# Please write your code here.
word1 = list(word1)
word2 = list(word2)
word1.sort()
word2.sort()

def fun(x, y):
    if len(x) != len(y):
        return False
    for elem1, elem2 in zip(x, y):
        if elem1 != elem2 :
            return False
    return True

if fun(word1, word2):
    print('Yes')
else :
    print('No')