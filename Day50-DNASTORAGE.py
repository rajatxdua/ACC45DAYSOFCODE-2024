T = int(input())
results = []

for _ in range(T):
    N = int(input())
    S = input()
    dna_map = {
        "00": "A",
        "01": "T",
        "10": "C",
        "11": "G"
    }
    encoded_sequence = ''.join(dna_map[S[i:i+2]] for i in range(0, N, 2))
    results.append(encoded_sequence)

print("\n".join(results))
