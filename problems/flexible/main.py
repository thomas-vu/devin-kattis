def calculate_possible_widths(W, partitions):
    possible_widths = set()
    
    # Include the width of the entire room
    possible_widths.add(W)
    
    # Include widths between each pair of partitions and the edges
    for i in range(len(partitions)):
        for j in range(i + 1, len(partitions) + 1):
            left = partitions[i] if i == 0 else partitions[i] - partitions[i-1]
            right = W - partitions[j-1] if j == len(partitions) else partitions[j] - partitions[j-1]
            possible_widths.add(left)
            possible_widths.add(right)
    
    # Include the width of each partition alone
    for partition in partitions:
        possible_widths.add(partition)
    
    return sorted(possible_widths)

# Main function to read input and output the result
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    W = int(data[0])
    P = int(data[1])
    partitions = list(map(int, data[2:]))
    
    result = calculate_possible_widths(W, partitions)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()