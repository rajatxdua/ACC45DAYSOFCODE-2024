t = int(input())
for _ in range(t):
    s, x, y, z = map(int, input().split())
    unused = s - (x + y)
    if unused >= z:
        print(0)
    elif unused + x >= z or unused + y >= z:
        print(1)
    else:
        print(2)

