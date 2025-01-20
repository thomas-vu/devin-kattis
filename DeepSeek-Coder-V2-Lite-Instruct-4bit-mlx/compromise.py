def min_hamming_distance(n, m, beliefs):
    best_agreement = None
    min_max_distance = float('inf')
    
    for j in range(m):
        bit_column = [belief[j] for belief in beliefs]
        count_zeros = bit_column.count('0')
        count_ones = bit_column.count('1')
        
        if count_zeros > n // 2:
            bit = '0'
        else:
            bit = '1'
        
        agreement = ['0'] * m
        agreement[j] = bit
        current_max_distance = 0
        
        for belief in beliefs:
            distance = sum(1 for i in range(m) if belief[i] != agreement[i])
            current_max_distance = max(current_max_distance, distance)
        
        if current_max_distance < min_max_distance:
            min_max_distance = current_max_distance
            best_agreement = agreement[:]
    
    return ''.join(best_agreement)

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        beliefs = [input() for _ in range(n)]
        result = min_hamming_distance(n, m, beliefs)
        print(result)

if __name__ == "__main__":
    main()