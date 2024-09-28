def is_easy_to_pronounce(S):
    vowels = set('aeiou')
    current_consonants = 0

    for char in S:
        if char not in vowels:
            current_consonants += 1
            if current_consonants >= 4:
                return "NO"
        else:
            current_consonants = 0
            
    return "YES"


T = int(input())

for _ in range(T):
    input()  
    S = input().strip()
    print(is_easy_to_pronounce(S))
