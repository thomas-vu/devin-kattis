def can_alex_win(n):
    # The key observation is that the first player (Alex) can always win if N is odd.
    # This is because on each turn, the first player can always subtract an amount that leaves an even number of cobblestones for the second player.
    # The process continues until there are an odd number of cobblestones left, at which point the first player will be forced to leave an even number for the second player,
    # who can then again force the first player to leave an odd number of cobblestones, and so on.
    # The only scenario where the first player loses is when N is even, because they will be forced to leave an odd number for the second player on their turn.
    return "YES" if n % 2 == 1 else "NO"

# Read the input
n = int(input().strip())

# Output the result
print(can_alex_win(n))