def count_odd_binomial_coefficients(N):
    # The number of odd coefficients in (1+x)^N is the same as the number of 1's
    # in the binary representation of N. This is because each coefficient (N choose k)
    # corresponds to a bit in the binary representation of N when considering the binomial expansion.
    count = 0
    while N > 0:
        count += N & 1
        N >>= 1
    return count

# Read the input
N = int(input().strip())

# Output the result
print(count_odd_binomial_coefficients(N))