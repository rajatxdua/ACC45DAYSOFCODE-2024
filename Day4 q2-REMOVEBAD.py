from collections import Counter

def min_operations_to_same(t, test_cases):
    results = []
    
    for n, a in test_cases:
        frequency = Counter(a)
        max_freq = max(frequency.values())
        operations = n - max_freq
        results.append(operations)
    
    return results

t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

results = min_operations_to_same(t, test_cases)
for result in results:
    print(result)
