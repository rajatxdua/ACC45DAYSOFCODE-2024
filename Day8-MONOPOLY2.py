t=int(input())
for i in range(t):
    p,q,r,s=map(int,input().split())
    if(p>(q+r+s)):
        print("yes")
    elif(q>(p+r+s)):
        print("yes")
    elif(r>(s+p+q)):
        print("yes")
    elif(s>(p+q+r)):
        print("yes")
    else:
        print("no")