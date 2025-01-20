import sys

def expected_matches(delta_l, delta_w, g, l):
    p = 0
    expected_matches = 0
    
    while True:
        if p == 100:
            break
        
        # Probability of winning and getting the prize
        win_and_prize = (100 - p) / 100 * g / 100
        
        # Probability of winning but not getting the prize
        win_but_no_prize = (100 - p) / 100 * (100 - g) / 100
        
        # Probability of losing
        lose = l / 100
        
        # Total probability of winning (including losing)
        total_win = win_and_prize + win_but_no_prize
        
        # Expected number of matches to get the prize for the first time
        if p == 0:
            expected_matches += (1 / total_win)
        else:
            expected_matches += (1 / total_win) * ((1 - win_and_prize) ** (p - 1))
        
        # Update p after a match
        if win_and_prize > 0:
            p = min(100, p + delta_w)
        else:
            p += (win_but_no_prize + lose) * delta_l
        
    return expected_matches

# Read input from stdin
input_line = sys.stdin.readline().strip()
delta_l, delta_w, g, l = map(int, input_line.split())

# Calculate and print the expected number of matches
result = expected_matches(delta_l, delta_w, g, l)
print("{:.10f}".format(result))