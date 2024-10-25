def count_contests(test_cases):
    for case in test_cases:
        N, contests = case
        start38_count = contests.count("START38")
        ltime108_count = contests.count("LTIME108")
        print(start38_count, ltime108_count)

T = int(input()) 
test_cases = []

for _ in range(T):
    N = int(input()) 
    contests = input().split() 
    test_cases.append((N, contests))

count_contests(test_cases)
