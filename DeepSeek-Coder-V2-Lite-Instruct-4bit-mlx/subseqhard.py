def count_interesting_subsequences(sequence):
    n = len(sequence)
    count = 0
    
    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += sequence[end]
            if current_sum == 47:
                count += 1
    
    return count

def main():
    T = int(input())
    for _ in range(T):
        input()  # consume the blank line
        N = int(input())
        sequence = list(map(int, input().split()))
        result = count_interesting_subsequences(sequence)
        print(result)

if __name__ == "__main__":
    main()