T = int(input())

for _ in range(T):
    N, X = map(int, input().split())
    subscriptions_needed = (N + 5) // 6  
    total_cost = subscriptions_needed * X
    print(total_cost)
