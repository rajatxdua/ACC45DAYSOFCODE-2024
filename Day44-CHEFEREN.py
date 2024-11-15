T = int(input())
for _ in range(T):
    N, A, B = map(int, input().split())
    odd_episodes = (N + 1) // 2
    even_episodes = N // 2
    total_duration = odd_episodes * B + even_episodes * A
    print(total_duration)
