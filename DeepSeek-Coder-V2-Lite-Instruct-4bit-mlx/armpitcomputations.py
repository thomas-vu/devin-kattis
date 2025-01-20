def min_instructions(target):
    if target == 0:
        return 0
    
    # Precompute the minimum instructions for all possible values in [0, 4095]
    min_instr = [float('inf')] * 4096
    min_instr[0] = 0
    
    for i in range(4096):
        if min_instr[i] != float('inf'):
            # ORWITH operation
            for v in range(16):
                new_val = i | v
                min_instr[new_val] = min(min_instr[new_val], min_instr[i] + 1)
            
            # LSL operation
            for amt in range(13):
                new_val = (i << amt) & 0xFFF
                min_instr[new_val] = min(min_instr[new_val], min_instr[i] + amt)
            
            # ROR operation
            for amt in range(13):
                new_val = (i >> amt) | ((i << (12 - amt)) & 0xFFF)
                min_instr[new_val] = min(min_instr[new_val], min_instr[i] + amt)
            
            # ADDONE operation
            new_val = (i + 1) % 4096
            min_instr[new_val] = min(min_instr[new_val], min_instr[i] + 1)
    
    return min_instr[target]

# Read input and process each test case
T = int(input())
for _ in range(T):
    target_value = int(input())
    print(min_instructions(target_value))