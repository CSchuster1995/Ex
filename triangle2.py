trng = int(input("How many triangles? "))
space = int(trng/2) ;
star = 1;
for i in range(0, int(trng/2)+1) :
    
    for j in range(space,-1,-1):
        print( " ",end="")
    for k in range(0,star):
        print("*",end="")

    space = space -1 
    star = star + 2 
    print("");