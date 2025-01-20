def xor_fibonacci(K, sequence, queries):
    # Precompute the sequence up to the maximum possible index
    max_index = 10**6 + 1
    xor_sequence = [0] * (max_index)
    
    # Compute the sequence using XOR operation
    for i in range(1, max_index):
        if i <= K:
            xor_sequence[i] = sequence[i - 1]
        else:
            xor_sequence[i] = xor_sequence[i - 1] ^ xor_sequence[i - K - 1]
    
    # Precompute the partial XORs for faster query processing
    xor_prefix = [0] * (max_index)
    for i in range(1, max_index):
        xor_prefix[i] = xor_sequence[i] ^ xor_prefix[i - 1]
    
    # Process the queries
    results = []
    for l, r in queries:
        if r >= max_index:
            # Adjust the range to fit within precomputed sequence
            l = (l - 1) % max_index + 1
            r = (r - 1) % max_index + 1
        results.append(xor_prefix[r] ^ xor_prefix[l - 1])
    
    return results

# Main function to handle input and output
def main():
    K = int(input())
    sequence = list(map(int, input().split()))
    Q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(Q)]
    
    # Process the queries and print results
    answers = xor_fibonacci(K, sequence, queries)
    for answer in answers:
        print(answer)

if __name__ == "__main__":
    main()