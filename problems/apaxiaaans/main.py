def compact_name(name):
    if not name:
        return ""
    
    compacted_name = [name[0]]  # Start with the first character
    
    for i in range(1, len(name)):
        if name[i] != name[i - 1]:
            compacted_name.append(name[i])
    
    return ''.join(compacted_name)

# Read input from the user
input_name = input()

# Output the compact version of the name
print(compact_name(input_name))