# Function to generate the new sequence of filenames based on the given permutation
def generate_filenames(n, perm):
    # Create a list of original filenames for reference
    original_filenames = [f"file{i+1}" for i in range(n)]
    
    # Create a list to store the new filenames with their original names
    new_filenames = [""] * n
    
    # Assign the original names to the new filenames based on the permutation
    for i, p in enumerate(perm):
        new_filenames[p - 1] = f"{i + 1}"
    
    # Return the new filenames in lexicographically increasing order
    return sorted(new_filenames)

# Main function to handle input and output
def main():
    # Read the number of tracks
    n = int(input())
    
    # Read the permutation of positions
    perm = list(map(int, input().split()))
    
    # Generate the new sequence of filenames
    result = generate_filenames(n, perm)
    
    # Output the new sequence of filenames
    print(" ".join(result))

# Call the main function to execute the program
if __name__ == "__main__":
    main()