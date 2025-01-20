def generate_array(N, matrix):
    # Initialize the array with zeros
    a = [0] * N
    
    # Iterate over the matrix to fill in the values of a
    for i in range(N):
        for j in range(i + 1, N):
            if matrix[i][j] != 0:
                a[i] |= (1 << j) if i == j else matrix[i][j]
                a[j] |= (1 << i) if i == j else matrix[i][j]
    
    return a

# Main function to read input, process the solution, and print the output
def main():
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = generate_array(N, matrix)
    print(*result)

# Call the main function to execute the program
if __name__ == "__main__":
    main()