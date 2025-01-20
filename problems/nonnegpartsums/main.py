def count_cyclic_shifts(sequence):
    n = len(sequence)
    prefix_sums = [0] * (n + 1)
    
    # Calculate prefix sums
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + sequence[i]
    
    count = 0
    for k in range(n):
        valid = True
        for i in range(1, n + 1):
            if prefix_sums[i] < prefix_sums[i - 1]:
                valid = False
                break
        if valid:
            count += 1
        # Rotate the sequence to the right by one position
        sequence = [sequence[-1]] + sequence[:-1]
    
    return count

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        sequence = list(map(int, input().split()))
        result = count_cyclic_shifts(sequence)
        print(result)

if __name__ == "__main__":
    main()