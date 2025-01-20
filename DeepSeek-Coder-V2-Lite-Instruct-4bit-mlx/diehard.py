def can_guarantee_win(dice1, dice2, dice3):
    def simulate_rolls(die1, die2, die3):
        wins = 0
        total_rolls = 100000
        for _ in range(total_rolls):
            roll1 = die1.pop(die1.index(max(die1)))
            roll2 = die2.pop(die2.index(max(die2)))
            roll3 = die3.pop(die3.index(max(die3)))
            if roll1 > roll2 and roll1 > roll3:
                wins += 1
            elif roll2 > roll1 and roll2 > roll3:
                wins += 1
            elif roll3 > roll1 and roll3 > roll2:
                wins += 1
            die1.append(roll1)
            die2.append(roll2)
            die3.append(roll3)
        return wins / total_rolls
    
    for i in range(1, 4):
        if simulate_rolls([x for x in dice1], [x for x in dice2], [x for x in dice3]) >= 0.5:
            return i
    return "No dice"

# Read input
dice1 = list(map(int, input().split()))
dice2 = list(map(int, input().split()))
dice3 = list(map(int, input().split()))

# Output the result
print(can_guarantee_win(dice1, dice2, dice3))