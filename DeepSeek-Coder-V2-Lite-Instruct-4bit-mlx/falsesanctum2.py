def find_key_length(s):
    n = len(s)
    # Create a list to store the lengths of the shortest substrings that can be repeated to form the original string
    lps = [0] * n
    
    # Compute the longest prefix which is also a suffix for each position in the string
    length = 0
    i = 1
    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    # The length of the key is the last element in lps plus one (if it's not zero)
    return n - lps[-1] if lps[-1] != 0 else n

# Read input from stdin
N = int(input())
S = input()

# Output the length of the key
print(find_key_length(S))