import sys

# Read the dictionary of words
dictionary = []
while True:
    word = sys.stdin.readline().strip()
    if word == '#':
        break
    dictionary.append(word)

# Read the message strings
messages = []
while True:
    line = sys.stdin.readline().strip()
    if line == '|':
        break
message = ''
for line in sys.stdin:
    if '|' in line:
        message += line.replace('|', '')
        messages.append(message)
        break
    message += line

# Function to find the maximum number of non-overlapping substrings
def max_non_overlapping_substrings(dictionary, message):
    n = len(message)
    dp = [0] * (n + 1)
    word_set = set(dictionary)
    
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        for j in range(i):
            if message[j:i] in word_set and (j == 0 or dp[j] > 0):
                dp[i] = max(dp[i], dp[j] + 1)
    
    return dp[n]

# Process each message string and output the result
for msg in messages:
    print(max_non_overlapping_substrings(dictionary, msg))