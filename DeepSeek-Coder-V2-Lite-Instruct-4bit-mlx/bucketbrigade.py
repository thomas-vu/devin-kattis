def calculate_time(n, v, x, f):
    # Calculate the number of buckets needed to transfer the water
    num_buckets = v / (n * x - f)
    # Calculate the time required for each bucket load
    time_per_load = (n * x - f) / f
    # Calculate the total time for all loads
    total_time = num_buckets * (2 * f + 2 * n * x)
    return total_time

def main():
    while True:
        try:
            # Read the input values for n, v, x, f, and t
            line = input().strip()
            if not line:
                continue
            n, v, x, f = map(float, line.split())
            n = int(n)
            # Calculate the total time required for each test case
            total_time = calculate_time(n, v, x, f)
            # Output the total time with appropriate precision
            print("{:.10f}".format(total_time))
        except EOFError:
            break

if __name__ == "__main__":
    main()