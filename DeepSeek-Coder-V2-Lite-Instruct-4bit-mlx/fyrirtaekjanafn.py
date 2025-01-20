def remove_consonants(name):
    vowels = "aeiou"
    return ''.join([char for char in name if char.lower() in vowels])

# Read input from stdin
name_suggestion = input().strip()

# Process the name suggestion and print the result
print(remove_consonants(name_suggestion))