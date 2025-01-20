import math

def approximate_cube_root(x):
    low, high = 0, x
    while low <= high:
        mid = (low + high) // 2
        cube = mid ** 3
        if cube == x:
            return mid
        elif cube < x:
            low = mid + 1
        else:
            high = mid - 1
    return low if abs(low**3 - x) < abs((low-1)**3 - x) else low - 1

def main():
    while True:
        try:
            x = int(input())
            print(approximate_cube_root(x))
        except EOFError:
            break

if __name__ == "__main__":
    main()