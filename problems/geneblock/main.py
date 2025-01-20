import math

def min_dirt_blocks(N):
    if N % 10 == 7:
        return math.ceil(N / 10)
    else:
        return -1

def main():
    t = int(input())
    for _ in range(t):
        N = int(input())
        print(min_dirt_blocks(N))

if __name__ == "__main__":
    main()