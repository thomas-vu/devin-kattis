def f(x):
    return (33 * x + 1) % (2 ** 20)

def generate_grid(X):
    grid = [[f(i * X + j) for j in range(X)] for i in range(X)]
    return grid

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    X = int(data[1])
    encrypted_message = data[2]
    
    grid = generate_grid(X)
    column_sums = [0] * X
    
    for j in range(X):
        for i in range(X):
            column_sums[j] = (column_sums[j] + grid[i][j]) % (2 ** 20)
    
    pad = ""
    for sum_val in column_sums:
        pad += chr(ord('A') + sum_val % 27)
    
    pad_length = len(pad)
    decrypted_message = ""
    
    for i in range(N):
        encrypted_char = ord(encrypted_message[i]) - ord('A')
        pad_char = ord(pad[i % pad_length]) - ord('A')
        decrypted_char = (encrypted_char - pad_char) % 27
        if decrypted_char == 26:
            decrypted_message += ' '
        else:
            decrypted_message += chr(ord('A') + decrypted_char)
    
    print(decrypted_message)

if __name__ == "__main__":
    main()