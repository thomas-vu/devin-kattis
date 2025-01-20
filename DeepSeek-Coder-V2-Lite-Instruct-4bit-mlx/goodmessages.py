def count_vowels_and_consonants(message):
    vowels = set('aeiouy')
    num_vowels = sum(1 for char in message if char in vowels)
    num_consonants = len(message) - num_vowels
    return num_vowels, num_consonants

def rotate_char(c, offset):
    if 'a' <= c <= 'z':
        return chr((ord(c) - ord('a') + offset) % 26 + ord('a'))
    return c

def apply_rotation_cipher(message, offset):
    encoded_message = ''.join(rotate_char(c, offset) for c in message)
    return encoded_message

def main():
    offset = int(input())
    message = input()
    num_steps = int(input())

    good_steps, bad_steps = 0, 0

    for _ in range(num_steps):
        encoded_message = apply_rotation_cipher(message, offset)
        num_vowels, num_consonants = count_vowels_and_consonants(encoded_message)
        if num_vowels * 2 < num_consonants:
            bad_steps += 1
        else:
            good_steps += 1
        message = encoded_message

    if bad_steps < good_steps:
        print("Boris")
    else:
        print("Colleague")

if __name__ == "__main__":
    main()