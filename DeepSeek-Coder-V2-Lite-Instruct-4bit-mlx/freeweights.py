def heaviest_dumbbell(n, weights1, weights2):
    combined_weights = []
    for w in weights1:
        combined_weights.append(w)
    for w in weights2:
        combined_weights.append(w)
    
    weight_count = {}
    for w in combined_weights:
        if w in weight_count:
            weight_count[w] += 1
        else:
            weight_count[w] = 1
    
    heaviest = 0
    for w, count in weight_count.items():
        if count % 2 == 1:
            heaviest = max(heaviest, w)
    
    return heaviest

# Sample Input 1
n = 5
weights1 = [2, 1, 8, 2, 8]
weights2 = [9, 9, 4, 1, 4]
print(heaviest_dumbbell(n, weights1, weights2))  # Output: 8

# Sample Input 2
n = 8
weights1 = [7, 7, 15, 15, 2, 2, 4, 4]
weights2 = [5, 5, 3, 3, 9, 9, 1, 10]
print(heaviest_dumbbell(n, weights1, weights2))  # Output: 10