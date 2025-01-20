def sodas_drunk(e, f, c):
    total_sodas = 0
    empty_bottles = e + f
    
    while empty_bottles >= c:
        new_sodas = empty_bottles // c
        total_sodas += new_sodas
        empty_bottles = empty_bottles % c + new_sodas
    
    return total_sodas

# Sample Input 1
e, f, c = 9, 0, 3
print(sodas_drunk(e, f, c))  # Output: 4

# Sample Input 2
e, f, c = 5, 5, 2
print(sodas_drunk(e, f, c))  # Output: 9