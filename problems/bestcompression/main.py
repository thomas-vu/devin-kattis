def can_compress(N, b):
    # Calculate the total number of bits required for N files each 1000 bits long
    total_bits = N * 1000
    
    # If b is less than or equal to 0, it's impossible to compress the files
    if b <= 0:
        return "no"
    
    # Check if the total number of bits can be compressed to at most b bits
    max_compressed_size = 2**b - 1
    
    if total_bits <= max_compressed_size:
        return "yes"
    else:
        return "no"

# Read the input
N, b = map(int, input().split())

# Output the result
print(can_compress(N, b))