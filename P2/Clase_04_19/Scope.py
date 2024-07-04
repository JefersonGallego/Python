x=6.02e23

def pi():
    global y
    y=3.1416
    print(y, id(y), sep=' ---> ')
    #print(N, id(N), sep=' ---> ')

def gravity():
    x=9.81
    print(x, id(x), sep=' ---> ')
    print(y, id(y), sep=' ---> ')

pi()
gravity()
print(y, id(y), sep=' ---> ') 

