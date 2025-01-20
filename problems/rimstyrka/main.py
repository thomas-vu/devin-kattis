def rhyme_power(words):
    def common_suffix_length(word1, word2):
        i = len(word1) - 1
        j = len(word2) - 1
        while i >= 0 and j >= 0 and word1[i] == word2[j]:
            i -= 1
            j -= 1
        return len(word1) - (i + 1), len(word2) - (j + 1)
    
    max_power = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            power = common_suffix_length(words[i], words[j])
            max_power = max(max_power, min(power))
    return max_power

# Read input
N = int(input())
words = [input().strip() for _ in range(N)]

# Calculate and print the result
print(rhyme_power(words))