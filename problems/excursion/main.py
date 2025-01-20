def min_swaps_to_organize(line):
    n = len(line)
    count0 = line.count('0')
    count1 = line.count('1')
    count2 = n - count0 - count1
    
    # The sequence should be 0s first, then 1s, and then 2s
    expected = '0' * count0 + '1' * count1 + '2' * count2
    swaps = 0
    
    for i in range(n):
        if line[i] != expected[i]:
            for j in range(i+1, n):
                if line[j] == expected[i]:
                    # Swap the elements at positions i and j
                    line = list(line)
                    line[i], line[j] = line[j], line[i]
                    line = ''.join(line)
                    swaps += 1
                    break
    
    return swaps

# Read the input from stdin
line = input().strip()

# Compute and print the result
print(min_swaps_to_organize(line))