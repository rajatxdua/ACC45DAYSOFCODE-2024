t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    s = (x + y) % 4
    if s in [0, 1]:
        print("Alice")
    elif s in [2, 3]:
        print("Bob")
