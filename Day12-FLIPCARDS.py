for i in range(int(input())):

    n, x =map(int, input().split())

    if x!=n:
        print(min(x, n-x))
    else:
        print(0)