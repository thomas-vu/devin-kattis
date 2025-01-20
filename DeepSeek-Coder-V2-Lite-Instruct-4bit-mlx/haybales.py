def min_operations(s):
    n = len(s)
    operations = 0
    
    while True:
        found_infected = False
        for i in range(n - 2):
            if s[i] == 'P' and s[i + 1] == 'P' and s[i + 2] == 'C':
                found_infected = True
                s = s[:i] + 'PPC' if s[i + 1] == 'C' else 'CPP'
                operations += 1
                break
        if not found_infected:
            break
    return operations

# Read input from the standard input
s = input().strip()
print(min_operations(s))