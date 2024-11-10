def is_cyclic_quadrilateral(T, test_cases):
    results = []
    for i in range(T):
        A, B, C, D = test_cases[i]
        if A + C == 180 and B + D == 180:
            results.append("YES")
        else:
            results.append("NO")
    return results

T = int(input())
test_cases = [list(map(int, input().split())) for _ in range(T)]
results = is_cyclic_quadrilateral(T, test_cases)
for result in results:
    print(result)
