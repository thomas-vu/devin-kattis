def parse_operations(ops):
    op_map = {}
    for op in ops:
        parts = op.split()
        code, cost = parts[0], int(parts[1])
        op_map[code] = cost
    return op_map

def apply_operations(op_map, word1, word2):
    cost = 0
    for op, w1_bit, w2_bit in zip(op_map, word1, word2):
        if op == 'N':
            continue
        elif op == 'F':
            cost += w1_bit != w2_bit
        elif op == 'S':
            cost += int(w1_bit == '0' and w2_bit == '1')
        elif op == 'C':
            cost += int(w1_bit == '1' and w2_bit == '0')
    return cost

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    index += 1
    
    results = []
    for _ in range(N):
        L = int(data[index])
        n_op = int(data[index + 1])
        n_w = int(data[index + 2])
        index += 3
        
        op_map = parse_operations(data[index:index + n_op])
        index += n_op
        
        words = data[index:index + n_w]
        index += n_w
        
        costs = []
        for word1, word2 in words:
            min_cost = float('inf')
            for op_code, cost in op_map.items():
                current_cost = apply_operations(op_code, word1, word2)
                min_cost = min(min_cost, current_cost)
            if min_cost == float('inf'):
                costs.append("NP")
            else:
                costs.append(str(min_cost))
        results.append(' '.join(costs))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()