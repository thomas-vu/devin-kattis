MOD = 10**9 + 7

def count_good_paintings(R, C):
    # There are 3 colors: R, G, B
    # Each edge must be painted with exactly one color
    # Each unit square has 4 edges, and each color is used for 2 edges
    # So, we need to count the number of valid ways to paint the canvas
    
    # For each unit square, we have 2 choices for the first color and 2 choices for the second color
    # So, there are 4 ways to paint each unit square's edges
    
    # However, the top-left and bottom-right corners of each unit square share edges with adjacent squares
    # This introduces some constraints, but since we have 3 colors, each edge must be painted differently
    
    # Let's calculate the number of ways to paint each row and column independently
    # Then, multiply these results since the rows and columns are independent in terms of painting edges
    
    # Number of ways to paint each row independently is 3^C, since there are C unit squares and 3 choices for each
    # Number of ways to paint each column independently is also 3^R, since there are R unit squares and 3 choices for each
    
    # However, we need to subtract the overcounted cases where all rows or all columns are painted with a single color
    # This happens in 3 ways for each (one for each color)
    
    total_ways = pow(3, R * C, MOD)
    subtract_single_color = 3 * pow(3, R - 1, MOD) * (C % MOD) + 3 * pow(3, C - 1, MOD) * (R % MOD)
    subtract_single_color -= 9  # Subtract the overcounted cases where all rows and columns are painted with a single color
    
    good_paintings = (total_ways - subtract_single_color) % MOD
    return good_paintings

# Read input and process each test case
T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    print(count_good_paintings(R, C))