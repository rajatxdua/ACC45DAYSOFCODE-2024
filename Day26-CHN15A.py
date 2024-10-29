t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    characteristics = list(map(int, input().split()))
    count = sum((value + k) % 7 == 0 for value in characteristics)
    print(count)

