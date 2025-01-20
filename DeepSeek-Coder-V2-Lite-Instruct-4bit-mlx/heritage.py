MOD = 1_000_000_007

def count_meanings(N, W, dictionary):
    word_to_meanings = {}
    for _ in range(N):
        word, meanings = dictionary[_].split()
        meanings = int(meanings)
        if word not in word_to_meanings:
            word_to_meanings[word] = []
        word_to_meanings[word].append(meanings)
    
    def dfs(index):
        if index == len(W):
            return 1
        count = 0
        for i in range(index, len(W)):
            if W[index:i+1] in word_to_meanings:
                for meaning in word_to_meanings[W[index:i+1]]:
                    count += dfs(i + 1) % MOD
        return count % MOD
    
    return dfs(0)

# Read input from stdin
N, W = map(str, input().split())
dictionary = [input() for _ in range(N)]

# Output the number of possible meanings
print(count_meanings(N, W, dictionary))