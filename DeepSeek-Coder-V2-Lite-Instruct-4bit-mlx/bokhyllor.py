def min_shelves(small, medium, big, shelf_width):
    # Calculate the total width occupied by books on each shelf
    def calculate_shelves(small, medium, big):
        total = small * 1 + medium * 2 + big * 3
        shelves_needed = (total + shelf_width - 1) // shelf_width  # Ceiling division
        return shelves_needed if shelves_needed >= 2 else 2
    
    # Try placing books on a single shelf first
    min_shelves = calculate_shelves(small, medium, big)
    
    # If we have more than 2 shelves, try to optimize by using up to 3 shelves
    if min_shelves > 2:
        for i in range(min_shelves - 1):
            # Try to fit as many big books on one shelf as possible
            while big > 0 and (small + medium) <= (shelf_width - 3):
                big -= 1
                small += 1
                medium += 1
            # Try to fit as many medium books on one shelf as possible
            while medium > 0 and (small + big) <= (shelf_width - 2):
                medium -= 1
                small += 1
            # Recalculate shelves needed after optimization
            min_shelves = calculate_shelves(small, medium, big)
            if min_shelves == 2:
                break
    
    return min_shelves

# Read input
small, medium, big = map(int, input().split())
shelf_width = int(input())

# Output the minimum number of shelves needed
print(min_shelves(small, medium, big, shelf_width))