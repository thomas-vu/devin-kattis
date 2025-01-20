def longest_common_prefix(word1, word2):
    min_len = min(len(word1), len(word2))
    for i in range(min_len):
        if word1[i] != word2[i]:
            return i
    return min_len

def calculate_steps(database, query):
    steps = 0
    for word in database:
        lcp_len = longest_common_prefix(word, query)
        steps += len(word) - lcp_len + 1
    return steps

def main():
    N = int(input())
    database = [input().strip() for _ in range(N)]
    Q = int(input())
    queries = [input().strip() for _ in range(Q)]
    
    for query in queries:
        print(calculate_steps([word.strip() for word in database], query))

if __name__ == "__main__":
    main()