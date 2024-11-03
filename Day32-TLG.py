N = int(input())
cumulative_score1 = cumulative_score2 = max_lead = winner = 0

for _ in range(N):
    score1, score2 = map(int, input().split())
    cumulative_score1 += score1
    cumulative_score2 += score2

    if cumulative_score1 > cumulative_score2:
        lead, current_leader = cumulative_score1 - cumulative_score2, 1
    else:
        lead, current_leader = cumulative_score2 - cumulative_score1, 2

    if lead > max_lead:
        max_lead, winner = lead, current_leader

print(winner, max_lead)

