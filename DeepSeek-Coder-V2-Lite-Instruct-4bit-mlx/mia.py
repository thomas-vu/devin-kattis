def mia_score(s0, s1, r0, r1):
    if (s0 == 2 and s1 == 1) or (s0 == 1 and s1 == 2):
        return "Player 1 wins."
    if (r0 == 2 and r1 == 1) or (r0 == 1 and r1 == 2):
        return "Player 2 wins."
    if s0 == s1 and r0 == r1:
        if s0 == 6 and r0 == 6:
            return "Player 1 wins." if s0 > r0 else "Player 2 wins."
        elif s0 == 6:
            return "Player 1 wins."
        elif r0 == 6:
            return "Player 2 wins."
        else:
            return "Player 1 wins." if s0 > r0 else ("Player 2 wins." if s0 < r0 else "Tie.")
    elif s0 == s1:
        return "Player 1 wins."
    elif r0 == r1:
        return "Player 2 wins."
    else:
        roll_scores = [str(max(s0, s1)) + str(min(s0, s1)), str(max(r0, r1)) + str(min(r0, r1))]
        roll_scores.sort(reverse=True)
        player_roll = int(roll_scores[0])
        opponent_roll = int(roll_scores[1])
        if player_roll > opponent_roll:
            return "Player 1 wins."
        elif player_roll < opponent_roll:
            return "Player 2 wins."
        else:
            return "Tie."

while True:
    s0, s1, r0, r1 = map(int, input().split())
    if s0 == 0 and s1 == 0 and r0 == 0 and r1 == 0:
        break
    result = mia_score(s0, s1, r0, r1)
    print(result)