from fractions import Fraction

def parse_roll(s):
    if s == '*':
        return None
    else:
        return int(s)

def get_score(roll):
    if roll is None:
        return float('inf')
    score = str(max(roll)) + str(min(roll)) if roll[0] != roll[1] else 2 * max(roll)
    return int(score)

def calculate_odds(s0, s1, r0, r1):
    player1_rolls = [parse_roll(s0), parse_roll(s1)]
    player2_rolls = [parse_roll(r0), parse_roll(r1)]
    
    player1_wins = 0
    total_outcomes = 0
    
    for p1_roll in player1_rolls:
        for p2_roll in player2_rolls:
            total_outcomes += 1
            if get_score(p1_roll) == float('inf') and get_score(p2_roll) == float('inf'):
                continue
            if get_score(p1_roll) > get_score(p2_roll):
                player1_wins += 1
            elif get_score(p1_roll) == get_score(p2_roll):
                if p1_roll[0] > p2_roll[0]:
                    player1_wins += 1
                elif p1_roll[0] == p2_roll[0] and p1_roll[1] > p2_roll[1]:
                    player1_wins += 1
    
    if player1_wins == 0:
        return 0
    elif player1_wins == total_outcomes:
        return 1
    else:
        return Fraction(player1_wins, total_outcomes)

while True:
    s0, s1, r0, r1 = input().split()
    if s0 == '0' and s1 == '0' and r0 == '0' and r1 == '0':
        break
    result = calculate_odds(s0, s1, r0, r1)
    if isinstance(result, Fraction):
        print(f"{result.numerator}/{result.denominator}")
    else:
        print(result)