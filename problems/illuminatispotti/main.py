def count_triangles(N, flight_matrix):
    triangle_count = 0
    
    for i in range(N):
        for j in range(i+1, N):
            if flight_matrix[i][j] == 1:
                for k in range(j+1, N):
                    if flight_matrix[i][k] == 1 and flight_matrix[j][k] == 1:
                        triangle_count += 1
    return triangle_count

# Read input
N = int(input().strip())
flight_matrix = [list(map(int, input().strip().split())) for _ in range(N)]

# Calculate and output the number of triangles
print(count_triangles(N, flight_matrix))