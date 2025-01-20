def count_okay_volumes(L, R, k, favorite_numbers):
    def is_valid_volume(vol):
        for num in favorite_numbers:
            if vol % num == 0:
                return True
        return False
    
    count = 0
    for vol in range(L, R + 1):
        if is_valid_volume(vol):
            count += 1
    return count

# Read input
L, R = map(int, input().split())
k = int(input())
favorite_numbers = list(map(int, input().split()))

# Calculate and output the result
n = count_okay_volumes(L, R, k, favorite_numbers)
print(n)