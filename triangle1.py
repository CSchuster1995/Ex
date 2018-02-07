space = 3 
star = 1
for i in range(0,4):


    for j in range(space,-1,-1):
        print( " ",end="")
       
    for k in range(0,star):
        print( u"\U0001F4A9",end="")
 
    star = star + 2
    space = space -1
    print("")