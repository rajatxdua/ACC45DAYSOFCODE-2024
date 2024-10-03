t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    
    a=500-2*x
    b=1000-4*(x+y)
    c=a+b
    k=1000-4*y
    l=500-2*(x+y)
    m=k+l
     
    if c>=m:
         print(c)
    else:
         print(m)