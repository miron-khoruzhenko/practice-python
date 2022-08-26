while True:
    x,y=map(int,input("НОД: ").split())

    while x!=y:
        if x>y:
            x-=y
        else:
            y-=x

    print(x)
