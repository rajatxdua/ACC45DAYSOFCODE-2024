T = int(input())
results = []

for _ in range(T):
    N = int(input())
    even_count = 0
    odd_count = 0

    for i in range(1, N + 1):
        if N % i == 0:
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    if even_count > odd_count:
        results.append(1)
    elif even_count == odd_count:
        results.append(0)
    else:
        results.append(-1)

print("\n".join(map(str, results)))
