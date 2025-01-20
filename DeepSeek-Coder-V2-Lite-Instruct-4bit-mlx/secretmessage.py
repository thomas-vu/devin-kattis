def encrypt_message(message):
    L = len(message)
    M = int(L**0.5 + 1)**2
    message += '*' * (M - L)
    
    K = int(M**0.5)
    table = [message[i*K:(i+1)*K] for i in range(M)]
    
    rotated_table = [''.join([table[x][y] for x in range(K-1, -1, -1)]) for y in range(K)]
    
    encrypted_message = ''.join([cell for row in rotated_table for cell in row if cell != '*'])
    return encrypted_message

N = int(input())
for _ in range(N):
    message = input()
    encrypted_message = encrypt_message(message)
    print(encrypted_message)