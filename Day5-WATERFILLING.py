def water_filling_time(test_cases):
    results = []
    for case in test_cases:
        empty_count = case.count(0)

        if empty_count >= 2:
            results.append("Water filling time")
        else:
            results.append("Not now")
    
    return results

T = int(input())
test_cases = []

for _ in range(T):
    B1, B2, B3 = map(int, input().split())
    test_cases.append([B1, B2, B3])

results = water_filling_time(test_cases)

for result in results:
    print(result)
