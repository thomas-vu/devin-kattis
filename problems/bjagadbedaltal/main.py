import sys

def geometric_mean(sequence):
    n = len(sequence)
    sorted_sequence = sorted(sequence)
    mean = sum(sorted_sequence) / n
    product = 1
    for x in sorted_sequence:
        product *= x
    geo_mean = product ** (1/n)
    median = sorted_sequence[(n-1)//2]
    return [mean, geo_mean, median]

def repeated_geometric_mean(sequence):
    while True:
        sequence = geometric_mean(sequence)
        if len(set(sequence)) == 1:
            return sequence[0]

# Read input
n = int(sys.stdin.readline().strip())
sequence = list(map(float, sys.stdin.readline().strip().split()))

# Calculate and print the geometric meandian
result = repeated_geometric_mean(sequence)
print("{:.15f}".format(result))