def check_cov(dna):
    return "Veikur!" if 'COV' in dna else "Ekki veikur!"

# Read input from stdin
dna_string = input().strip()

# Output the result
print(check_cov(dna_string))