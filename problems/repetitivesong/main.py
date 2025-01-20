def longest_non_identifiable_subsequence(song):
    word_indices = {}
    for i, word in enumerate(song):
        if word not in word_indices:
            word_indices[word] = []
        word_indices[word].append(i)
    
    def is_identifiable(subseq):
        last_index = -1
        for index in subseq:
            if index <= last_index:
                return False
            last_index = index
        return True
    
    max_length = 0
    for word, indices in word_indices.items():
        n = len(indices)
        for mask in range(1, 1 << n):
            subseq_indices = [indices[i] for i in range(n) if (mask & (1 << i))]
            if is_identifiable(subseq_indices):
                max_length = max(max_length, len(subseq_indices))
    
    return max_length

# Read input
n = int(input().strip())
song = [input().strip() for _ in range(n)]

# Output the result
print(longest_non_identifiable_subsequence(song))