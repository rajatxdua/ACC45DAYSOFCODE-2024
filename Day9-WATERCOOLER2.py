for i in range(int(input())):
    x,y=map(int,input().split())
    if x>=y:
        print('0')
    elif x<y and y%x!=0:
        print(y//x)
    else:
        print((y//x)-1)