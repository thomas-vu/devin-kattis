def is_arithmetic(seq):
    diff = seq[1] - seq[0]
    for i in range(2, len(seq)):
        if seq[i] - seq[i-1] != diff:
            return False
    return True

def is_permuted_arithmetic(seq):
    seq.sort()
    original_diff = seq[1] - seq[0]
    for i in range(2, len(seq)):
        if seq[i] - seq[i-1] != original_diff:
            return False
    return True

n = int(input())
for _ in range(n):
    seq_info = list(map(int, input().split()))
    m = seq_info[0]
    sequence = seq_info[1:]
    
    if is_arithmetic(sequence):
        print("arithmetic")
    elif is_permuted_arithmetic(list(sequence)):
        print("permuted arithmetic")
    else:
        print("non-arithmetic")