def rotate_string(s, rotation):
    rotated = ""
    for char in s:
        new_char = chr(((ord(char) - ord('A') + rotation) % 26) + ord('A'))
        rotated += new_char
    return rotated

def decrypt_drm(message):
    half = len(message) // 2
    left, right = message[:half], message[half:]
    
    # Calculate rotation values for each half
    left_sum = sum(ord(char) - ord('A') for char in left)
    right_sum = sum(ord(char) - ord('A') for char in right)
    
    # Rotate each half
    rotated_left = rotate_string(left, left_sum)
    rotated_right = rotate_string(right, right_sum)
    
    # Merge the rotated halves
    decrypted = ""
    for i in range(half):
        new_char = rotate_string([rotated_left[i]], ord(rotated_right[i]) - ord('A'))[0]
        decrypted += new_char
    
    return decrypted

# Read input from stdin
input_message = input().strip()
print(decrypt_drm(input_message))