def cast_sources(your_source, opponent_source):
    # Define the casting table for the sources
    cast_table = [
        [0, 1, 2, 3],
        [1, 0, -3, 4],
        [2, 3, 0, -1],
        [3, -2, 1, 0]
    ]
    
    # Convert the sources to a common form for easier calculations
    def parse_source(s):
        r, i, j, k = 0, 0, 0, 0
        if 'R' in s: r = int(s.split('R')[0])
        if 'I' in s: i = int(s.split('I')[0].replace(' ', ''))
        if 'J' in s: j = int(s.split('J')[0].replace(' ', ''))
        if 'K' in s: k = int(s.split('K')[0].replace(' ', ''))
        return r, i, j, k
    
    def right_cast(x, y):
        return cast_table[x][y]
    
    def left_cast(x, y):
        return cast_table[y][x]
    
    # Parse the sources
    your_r, your_i, your_j, your_k = parse_source(your_source)
    opp_r, opp_i, opp_j, opp_k = parse_source(opponent_source)
    
    # Perform the right cast on your source with the opponent's source
    new_your_r = your_r * opp_r - (your_i * opp_j + your_j * opp_k + your_k * opp_i)
    new_your_i = your_r * opp_i + your_i * opp_r + (your_j * opp_k - your_k * opp_j)
    new_your_j = your_r * opp_j - your_i * opp_k + your_j * opp_r + your_k * opp_i
    new_your_k = your_r * opp_k + your_i * opp_j - your_j * opp_i + your_k * opp_r
    
    return new_your_r, new_your_i, new_your_j, new_your_k

# Read inputs
your_source = input().strip()
opponent_source = input().strip()

# Calculate the resulting source after casting
new_your_r, new_your_i, new_your_j, new_your_k = cast_sources(your_source, opponent_source)

# Output the result
print(new_your_r, new_your_i, new_your_j, new_your_k)