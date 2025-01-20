def transform_long_to_short(name):
    names = name.split('-')
    short_variation = ''.join(n[0] for n in names)
    return short_variation

# Read input from stdin
input_line = input().strip()

# Transform the long variation to short and print the result
print(transform_long_to_short(input_line))