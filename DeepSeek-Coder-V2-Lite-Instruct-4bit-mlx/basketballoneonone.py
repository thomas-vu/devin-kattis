def determine_winner(record):
    alice_score = 0
    barbara_score = 0
    
    i = 0
    while i < len(record):
        if record[i] == 'A':
            alice_score += int(record[i+1])
        else:
            barbara_score += int(record[i+1])
        i += 2
        
    if alice_score >= 11 and (alice_score - barbara_score) >= 2:
        return 'A'
    elif barbara_score >= 11 and (barbara_score - alice_score) >= 2:
        return 'B'
    else:
        raise ValueError("The game is still ongoing or the rules are not followed.")

record = input().strip()
winner = determine_winner(record)
print(winner)