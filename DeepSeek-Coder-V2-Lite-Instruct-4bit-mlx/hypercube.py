def gray_code(n):
    code = [0]
    for i in range(1, n + 1):
        code += [x + (1 << (i - 1)) for x in reversed(code)]
    return code

def count_vertices(a, b):
    n = len(a)
    gray_code_sequence = gray_code(n)
    
    index_a = gray_code_sequence.index(int(a, 2))
    index_b = gray_code_sequence.index(int(b, 2))
    
    return abs(index_a - index_b)

# Read input
n, a, b = int(input().split()[0]), input().split()[1], input().split()[2]

# Output the result
print(count_vertices(a, b))