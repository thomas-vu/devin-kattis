def collide(n, m):
    n_str = str(n)
    m_str = str(m)
    
    min_len = min(len(n_str), len(m_str))
    
    new_n = ""
    new_m = ""
    
    for i in range(min_len):
        if int(n_str[i]) > int(m_str[i]):
            new_n += n_str[i]
        elif int(m_str[i]) > int(n_str[i]):
            new_m += m_str[i]
    
    if len(new_n) == 0:
        new_n = "YODA"
    if len(new_m) == 0:
        new_m = "YODA"
    
    return new_n, new_m

# Read inputs
N = int(input())
M = int(input())

# Get the new values after collision
new_N, new_M = collide(N, M)

# Output the results
print(new_N)
print(new_M)