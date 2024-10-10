t=int(input())

for i in range(t):

    a,b=map(int,input().split())
    if b/a >= 0.5:
        print("YES")
        
    else:
        print("NO")