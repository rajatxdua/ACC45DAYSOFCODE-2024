T = int(input())
for _ in range(T):
    N, X, P = map(int, input().split())
    score = X * 3 - (N - X)
    if score >= P:
        print("PASS")
    else:
        print("FAIL")
