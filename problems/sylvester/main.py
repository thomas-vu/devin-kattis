def hadamard_matrix(n):
    if n == 1:
        return [[1]]
    H_n = hadamard_matrix(n // 2)
    top_left = H_n
    top_right = H_n
    bottom_left = H_n
    bottom_right = [[-x for x in row] for row in H_n]
    return [row1 + row2 for row1, row2 in zip(top_left + top_right, bottom_left + bottom_right)]

def print_submatrix(n, x, y, w, h):
    H = hadamard_matrix(n)
    submatrix = [row[x:x+w] for row in H[y:y+h]]
    for row in submatrix:
        print(" ".join(str(x) for x in row))
    print()

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    
    for _ in range(t):
        n = int(data[index])
        x = int(data[index + 1])
        y = int(data[index + 2])
        w = int(data[index + 3])
        h = int(data[index + 4])
        index += 5
        print_submatrix(n, x, y, w, h)

if __name__ == "__main__":
    main()