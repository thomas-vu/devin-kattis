def find_longest_word(input_string):
    words = input_string.split()
    max_length = 0
    longest_word = ""
    
    for word in words:
        length = len(word)
        if length > max_length:
            max_length = length
            longest_word = word
    
    return longest_word

# Read input from stdin
input_string = ""
while True:
    try:
        line = input()
        input_string += line + " "
    except EOFError:
        break

# Process the input string to find the longest word
longest_word = find_longest_word(input_string.strip())

# Output the result
print("D")
print(len(longest_word))