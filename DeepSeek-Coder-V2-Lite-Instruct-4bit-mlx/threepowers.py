def find_subset(n):
    powers_of_3 = [3**i for i in range(16)]  # Generate powers of 3 up to 3^15
    subset = []
    i = len(powers_of_3) - 1
    while n > 0 and i >= 0:
        if n >= powers_of_3[i]:
            subset.append(powers_of_3[i])
            n -= powers_of_3[i]
        i -= 1
    return sorted(subset)

while True:
    n = int(input())
    if n == 0:
        break
    subset = find_subset(n)
    print("{ " + ", ".join(map(str, subset)) + " }")