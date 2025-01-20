def find_k(L, message, crypto_text, substitution_table):
    def encrypt_once(message, substitution_table):
        return [substitution_table[x - 1] for x in message]

    def encrypt(message, substitution_table, k):
        encrypted = message[:]
        for _ in range(k):
            encrypted = encrypt_once(encrypted, substitution_table)
        return encrypted

    def is_valid_k(k):
        return encrypt(crypto_text, substitution_table, k) == message

    left, right = 0, 10**9
    while left <= right:
        mid = (left + right) // 2
        if is_valid_k(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    index += 1
    results = []
    
    for _ in range(N):
        L = int(data[index])
        index += 1
        message = list(map(int, data[index:index + L]))
        index += L
        crypto_text = list(map(int, data[index:index + L]))
        index += L
        substitution_table = list(map(int, data[index:index + 100]))
        index += 100
        k = find_k(L, message, crypto_text, substitution_table)
        results.append(k)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()