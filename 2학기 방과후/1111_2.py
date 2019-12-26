a=""

for i in range(1,10,1):
    a=""
    for j in range(9,1,-1):
        a+=str("%2d X%2d =%2d"%(j,i,i*j))
        
        
    print(a)


