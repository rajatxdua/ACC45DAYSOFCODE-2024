def min_coins_required(test_cases, gifts):
    results = []
    for n in gifts:
        results.append(n - (n // 5))
    return results

T = int(input())
gifts = [int(input()) for _ in range(T)]
results = min_coins_required(T, gifts)
for res in results:
    print(res)
