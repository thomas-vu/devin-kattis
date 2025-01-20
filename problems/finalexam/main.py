def count_right_triangles(na, nb, nc, a, b, c):
    # Count the frequency of each segment length
    freq_a = {x: 0 for x in a}
    freq_b = {x: 0 for x in b}
    freq_c = {x: 0 for x in c}
    
    for length in a:
        freq_a[length] += 1
    for length in b:
        freq_b[length] += 1
    for length in c:
        freq_c[length] += 1
    
    count = 0
    
    # Check all possible combinations to form a right triangle
    for ai in freq_a:
        for bi in freq_b:
            if (ai**2 + bi**2)**.5 == int((ai**2 + bi**2)**.5):
                # Check if the square root of ai^2 + bi^2 exists in the third pile
                ci = int((ai**2 + bi**2)**.5)
                if ci in freq_c:
                    count += freq_a[ai] * freq_b[bi] * freq_c[ci]
            if ai**2 + bi**2 == bi**2 + ai**2:  # Check for the other possible right triangle
                count += freq_a[ai] * freq_b[bi] * freq_c[ci]
    
    return count

# Read input
na, nb, nc = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

# Count the number of ways to form right triangles
result = count_right_triangles(na, nb, nc, a, b, c)
print(result)