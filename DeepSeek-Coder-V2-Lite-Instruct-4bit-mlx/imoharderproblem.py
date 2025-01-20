def calculate_average_operations(sequence):
    n = len(sequence)
    expected_value = 0.0
    
    for mask in range(1 << n):
        current_sequence = list(sequence)
        operations = 0
        
        for _ in range(n):
            count_H = sum(1 for i in range(n) if (mask >> i) & 1 == 1 and current_sequence[i] == 'H')
            if count_H > 0:
                for i in range(n):
                    if (mask >> i) & 1 == 1:
                        current_sequence[i] = 'H' if current_sequence[i] == 'T' else 'T'
            else:
                break
            operations += 1
        
        expected_value += operations
    
    expected_value /= (1 << n)
    return expected_value

sequence = input().strip()
result = calculate_average_operations(sequence)
print("{:.1f}".format(result))