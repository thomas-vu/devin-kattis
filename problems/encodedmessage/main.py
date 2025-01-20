import math

def decode_message(encoded):
    n = int(math.sqrt(len(encoded)))
    original = ''
    for i in range(n):
        for j in reversed(range(i, len(encoded), n)):
            original += encoded[j]
    return original

def main():
    num_cases = int(input())
    for _ in range(num_cases):
        encoded = input().strip()
        print(decode_message(encoded))

if __name__ == "__main__":
    main()