for i in range(1,10):
    for m in range(1,i):
        print(end='           ')
    for j in range(i,10):  
        print("%2dx%2d=%2d" % (i,j,i*j),end='   ')
    print()
   