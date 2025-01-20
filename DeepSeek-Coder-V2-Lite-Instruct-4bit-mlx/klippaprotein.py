def min_cuts(protein, K):
    n = len(protein)
    cuts = 0
    
    while True:
        count = {}
        for char in protein:
            count[char] = count.get(char, 0) + 1
        
        max_count = max(count.values())
        if max_count <= K:
            break
        
        min_length = float('inf')
        for char in count:
            if count[char] > K:
                temp_protein = protein.split(char)
                total_length = sum(len(part) for part in temp_protein)
                min_length = min(min_length, total_length)
        
        protein = protein[:min_length] + protein[min_length+1:]
        cuts += 1
    
    return cuts

# Read input from stdin
protein = input().strip()
K = int(input().strip())

# Calculate and print the result
print(min_cuts(protein, K))