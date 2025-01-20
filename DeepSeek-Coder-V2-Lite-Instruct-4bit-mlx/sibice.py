import sys

def main():
    # Read the number of matches and the dimensions of the box
    N, W, H = map(int, sys.stdin.readline().split())
    
    # Calculate the diagonal of the box
    max_length = (W**2 + H**2)**0.5
    
    # Process each match and determine if it fits in the box
    for _ in range(N):
        length = int(sys.stdin.readline())
        if length <= max_length:
            print("DA")
        else:
            print("NE")

if __name__ == "__main__":
    main()