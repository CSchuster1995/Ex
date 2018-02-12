def word_histogram(string):
    mydict={}
    wordlist = string.lower().split()
    for i in range(len(wordlist)):
        if wordlist[i] in mydict.keys():
            mydict[wordlist[i]] = mydict[wordlist[i]] + 1
        else:
            mydict[wordlist[i]] = 1
    return mydict

res = word_histogram("What what it do")
print(res)