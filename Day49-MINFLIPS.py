t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    A = list(map(int, input().split()))
    c1 = sum(1 for x in A if x == 1)
    c2 = n - c1
    
    ans = abs((c1 - c2) // 2)
    if n % 2 != 0:
        print(-1)
    else:
        print(ans)
