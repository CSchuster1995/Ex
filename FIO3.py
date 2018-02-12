f = input("Which file would you like to open? ")

def letter_histogram(word):
    mydict={}
    for i in range(0, len(word)):
        if word[i] in mydict.keys():
            mydict[word[i]] = mydict[word[i]] + 1
        else:
            mydict[word[i]] = 1
    return mydict


res = letter_histogram("banana")
print(res)