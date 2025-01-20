def who_wins(k, m, n):
    if k <= m:
        return "Alex"
    
    def can_win(k, m, n):
        for x in range(m, n + 1):
            if k % (m + n) <= m and k % (m + n) != 0:
                return True
        return False
    
    if can_win(k, m, n):
        return "Alex"
    else:
        return "Barb"

# Read input
k, m, n = map(int, input().split())

# Determine the winner and print the result
winner = who_wins(k, m, n)
print(winner)