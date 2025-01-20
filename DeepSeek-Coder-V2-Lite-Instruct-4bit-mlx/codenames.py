def is_swap_free(word1, word2):
    return sorted(word1) == sorted(word2)

def find_largest_swap_free_set(words):
    n = len(words)
    max_set_size = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            if is_swap_free(words[i], words[j]):
                count = 2
                for k in range(j + 1, n):
                    if is_swap_free(words[i], words[k]) and is_swap_free(words[j], words[k]):
                        count += 1
                max_set_size = max(max_set_size, count)
    
    return max_set_size

# Read input
N = int(input())
words = [input().strip() for _ in range(N)]

# Output the result
print(find_largest_swap_free_set(words))