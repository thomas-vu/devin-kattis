def is_valid_message(password, message):
    password_set = set(password)
    index = 0
    
    for char in password:
        found_index = message.find(char, index)
        if found_index == -1:
            return "FAIL"
        index = found_index + 1
    
    for i in range(len(password)):
        next_char = chr(ord(password[i]) + 1)
        found_index = message.find(next_char, index)
        if found_index == -1:
            return "FAIL"
        index = found_index + 1
    
    return "PASS"

# Read input
password, message = input().split()

# Output the result
print(is_valid_message(password, message))