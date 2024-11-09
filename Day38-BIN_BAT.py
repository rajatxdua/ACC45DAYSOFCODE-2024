T = int(input())

for _ in range(T):
    N, A, B = map(int, input().split())
    
    total_time = 0
    rounds = 0
    
    while N > 1:
        total_time += A
        rounds += 1
        N //= 2
    
    total_time += B * (rounds - 1)
    
    print(total_time)
