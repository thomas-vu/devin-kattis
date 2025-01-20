def winning_games(scores):
    alice_wins = 0
    bob_wins = 0
    game_lengths = []
    
    i = 0
    while i < len(scores):
        start = i
        while i < len(scores) and scores[i] == scores[start]:
            i += 1
        game_lengths.append(i - start)
    
    max_k = min(max(game_lengths), 11)
    
    for k in range(2, max_k + 1):
        alice_points = 0
        bob_points = 0
        for length in game_lengths:
            if length >= k:
                alice_points += (length + 1) // 2
                bob_points += length // 2
        
        if alice_points > bob_points:
            alice_wins += 1
    
    if alice_wins == 0:
        print(0)
    else:
        possible_ks = [k for k in range(2, max_k + 1) if alice_wins > (len(game_lengths) - alice_wins)]
        print(len(possible_ks))
        print(" ".join(map(str, sorted(possible_ks))))

# Read input
scores = input().strip()
winning_games(scores)