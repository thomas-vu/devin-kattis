MOD = 1_000_000_007

def mod_pow(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def count_drafts(n):
    if n < 20:
        return 0
    
    # Calculate the number of ways to distribute bans and picks for each team
    blue_bans = mod_pow(n - 20, 5, MOD)
    red_bans = mod_pow(n - 20, 5, MOD)
    blue_picks = mod_pow(n - 20 + 1, 5, MOD) * mod_pow(n - 20 + 2, 10, MOD)
    red_picks = mod_pow(n - 20 + 3, 5, MOD) * mod_pow(n - 20 + 4, 10, MOD)
    
    # Total number of ways for bans and picks
    total_ways = (blue_bans * red_bans * blue_picks * red_picks) % MOD
    
    # Calculate the number of ways to distribute bans and picks for each step
    blue_bans = mod_pow(n - 20, 5, MOD)
    red_bans = mod_pow(n - 20, 5, MOD)
    blue_picks = mod_pow(n - 20 + 1, 5, MOD) * mod_pow(n - 20 + 2, 10, MOD)
    red_picks = mod_pow(n - 20 + 3, 5, MOD) * mod_pow(n - 20 + 4, 10, MOD)
    
    # Total number of ways for bans and picks
    total_ways = (blue_bans * red_bans * blue_picks * red_picks) % MOD
    
    return total_ways

# Read input
n = int(input().strip())

# Calculate and output the result
result = count_drafts(n)
print(result)