import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_gcd(lst):
    num = lst[0]
    for i in lst[1:]:
        num = gcd(num, i)
    return num

def base3_representation(number):
    if number == 0:
        return "0"
    result = ""
    while number > 0:
        remainder = number % 3
        result = str(remainder) + result
        number //= 3
    return result

def encode_word(word):
    ascii_values = [ord(char) for char in word]
    key = find_gcd(ascii_values)
    encoded_values = [str(base3_representation(value // key)) for value in ascii_values]
    return key, " ".join(encoded_values)

def encode_message(message):
    words = message.split()
    encoded_output = []
    for word in words:
        key, encoded_word = encode_word(word)
        encoded_output.append(f"{key}\n{encoded_word}")
    return "\n".join(encoded_output)

# Example usage:
message = "Fix it"
print(encode_message(message))