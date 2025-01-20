def main():
    n = int(input())
    cans = [tuple(map(int, input().split())) for _ in range(n)]
    # Sort cans by their x-coordinate to process them from left to right
    cans.sort(key=lambda x: x[0])
    
    # Create a list to store the number of cans that will explode for each can
    explosions = [0] * n
    
    # Process the cans from left to right
    for i in range(n):
        x_i, r_i = cans[i]
        # Count the number of cans that will explode if this can is shot
        count = 0
        for j in range(n):
            if i != j:
                x_j, r_j = cans[j]
                # Check if the j-th can is within the blast radius of the i-th can
                if abs(x_i - x_j) <= r_i:
                    count += 1
        explosions[i] = count + 1  # Include the can itself in the explosion count
    
    # Print the number of explosions for each can
    print(' '.join(map(str, explosions)))

if __name__ == "__main__":
    main()