import math

def min_breaks(K):
    size = 1
    breaks = 0
    while size < K:
        size *= 2
        breaks += 1
    
    return (size, breaks)

def main():
    K = int(input())
    size, breaks = min_breaks(K)
    print(size, breaks)

if __name__ == "__main__":
    main()