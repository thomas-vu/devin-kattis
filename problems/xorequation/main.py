def count_ways(a, b, c):
    a_str = str(a)
    b_str = str(b)
    c_str = str(c)
    
    count = 0
    for i in range(10**len(a_str)):
        a_i = int(a_str.replace('?', str(i)))
        for j in range(10**len(b_str)):
            b_j = int(b_str.replace('?', str(j)))
            for k in range(10**len(c_str)):
                c_k = int(c_str.replace('?', str(k)))
                if (a_i ^ b_j) == c_k:
                    count += 1
    return count

# Read input
input_line = input().strip()
parts = input_line.split(' xor ')
left, right = parts[0].split(' = '), parts[1]
a = int(left[0])
b = int(parts[0].split(' xor ')[1])
c = int(right.replace('=', '').strip())

# Calculate and print the number of ways
print(count_ways(a, b, c))