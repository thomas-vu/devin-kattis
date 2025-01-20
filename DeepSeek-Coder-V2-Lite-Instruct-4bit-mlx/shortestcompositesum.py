import sys
import math

# Function to check if a number is composite
def is_composite(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return True
    return False

# Main function to find the shortest sequence of composite numbers summing to N
def main():
    # Read input
    N = int(sys.stdin.readline().strip())
    
    # Start with the smallest composite number and keep adding more until sum >= N
    i = 4
    sequence = []
    while N > 0:
        if is_composite(i):
            sequence.append(i)
            N -= i
        i += 1
    
    # Output the result
    print(len(sequence))
    print(' '.join(map(str, sequence)))

# Run the main function
if __name__ == "__main__":
    main()