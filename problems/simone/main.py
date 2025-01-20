from collections import Counter
import sys

def main():
    # Read input from stdin
    N, K = map(int, sys.stdin.readline().split())
    sequence = list(map(int, sys.stdin.readline().split()))
    
    # Count the frequency of each color in the sequence
    color_count = Counter(sequence)
    
    # Find the minimum frequency
    min_frequency = min(color_count.values())
    
    # Find all colors with the minimum frequency
    least_frequent_colors = [color for color, count in color_count.items() if count == min_frequency]
    
    # Output the result
    print(len(least_frequent_colors))
    print(" ".join(map(str, sorted(least_frequent_colors))))

if __name__ == "__main__":
    main()