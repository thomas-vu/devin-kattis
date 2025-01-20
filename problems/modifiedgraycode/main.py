def even_gray_code(index):
    code = ['0'] * 10
    used = set()
    
    def count_differing_bits(a, b):
        return sum(1 for x, y in zip(a, b) if x != y)
    
    def generate_even_gray_code(index, code):
        if index == 0:
            return ''.join(code)
        
        for i in range(10):
            for j in range(i + 1, 10):
                new_code = list(code)
                new_code[i] = '1' if new_code[i] == '0' else '0'
                new_code[j] = '1' if new_code[j] == '0' else '0'
                new_code_str = ''.join(new_code)
                
                if new_code_str not in used:
                    used.add(new_code_str)
                    if count_differing_bits(new_code_str, index_to_gray_code(index - 1)) % 2 == 0:
                        return generate_even_gray_code(index - 1, new_code)
                    used.remove(new_code_str)
        return ''
    
    def index_to_gray_code(n):
        return n ^ (n >> 1)
    
    index_gray = index_to_gray_code(index - 1)
    code[0] = '1' if index_gray & (1 << 9) else '0'
    code[1] = '1' if index_gray & (1 << 8) else '0'
    
    used.add(''.join(code))
    return generate_even_gray_code(index - 1, code)
    
# Read input
N = int(input())
queries = [int(input()) for _ in range(N)]

# Process each query and print the result
for k in queries:
    print(even_gray_code(k))