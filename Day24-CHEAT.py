def count_tuesdays(N):
    return (N + 5) // 7

T = int(input().strip())
results = [count_tuesdays(int(input().strip())) for _ in range(T)]
print("\n".join(map(str, results)))
