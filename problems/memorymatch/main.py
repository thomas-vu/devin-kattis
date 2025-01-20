def find_matching_pairs(N, turns):
    card_pictures = {}
    
    for turn in turns:
        C1, C2, P1, P2 = turn
        if (C1, P1) not in card_pictures and (C2, P2) not in card_pictures:
            if P1 == P2:
                card_pictures[(C1, P1)] = True
                card_pictures[(C2, P2)] = True
    
    return len(card_pictures) // 2

# Read input
N = int(input())
K = int(input())
turns = []
for _ in range(K):
    C1, C2, P1, P2 = input().split()
    turns.append((int(C1), int(C2), P1, P2))

# Calculate and print the result
S = find_matching_pairs(N, turns)
print(S)