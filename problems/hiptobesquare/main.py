import math

def max_layers(N):
    # The size of the square with an empty 1x1 in the middle is (2k+1) x (2k+1),
    # where k is the number of layers. The total number of tiles in this square is (2k+1)^2 - 1,
    # because there's one empty tile in the middle.
    k = int(math.sqrt((N + 1) / 2))
    # The number of tiles used for the square with an empty tile in the middle is (2k+1)^2 - 1
    tiles_used = (2 * k + 1) ** 2 - 1
    # The remaining tiles are the total tiles minus the tiles used for the square.
    remaining_tiles = N - tiles_used
    return k

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(max_layers(N))

if __name__ == "__main__":
    main()