def max_plates(test_cases, data):
    results = []
    for x, y, r in data:
        extra_sticks = r // 30
        total_sticks = x + extra_sticks
        plates = (total_sticks + y - 1) // y
        results.append(plates)
    return results

T = int(input())
data = [tuple(map(int, input().split())) for _ in range(T)]
results = max_plates(T, data)
for res in results:
    print(res)
