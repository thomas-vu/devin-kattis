def calculate_score(notes):
    truls = 0
    henry = 0
    
    for note in notes:
        if note == 'T':
            truls += 1
        elif note == 'H':
            henry += 1
    
    return f"{truls}-{henry}"

# Test cases
print(calculate_score("TTTHHHTHH"))  # Output: 4-5
print(calculate_score("TTTTTTTTT") ) # Output: 0-0
print(calculate_score("THTHTHTHTHTHTHTHTHTH"))  # Output: 12-12
print(calculate_score("THTHTHT"))  # Output: 0-1