def find_key(N, words, A):
    # Create a dictionary to map each word to its position in array A
    pos_map = {A[i]: words[i] for i in range(N)}
    
    # Create a dictionary to map each letter to its position in the key
    key_map = {}
    
    # Determine the order of letters based on the words and their positions in A
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        for i in range(1, N + 1):
            word = pos_map[i]
            if letter in word:
                key_map[letter] = word.index(letter) + 1
                break
    
    # Check if the key can be determined uniquely
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter not in key_map:
            for i, word in pos_map.items():
                if letter in word and word.index(letter) + 1 > key_map[letter]:
                    return "NE"
    
    # Construct the key based on the determined order of letters
    key = ''.join(sorted(key_map, key=lambda x: key_map[x]))
    
    return "DA", key

# Read input
N = int(input())
words = [input() for _ in range(N)]
A = list(map(int, input().split()))

# Get the result
result, key = find_key(N, words, A)
print(result)
if result == "DA":
    print(key)