def unscramble(n, bytes_list):
    def unshift(byte):
        return byte ^ (byte << 1)
    
    def shift(byte):
        return byte >> 1 if byte & 1 == 0 else (byte >> 1) | 128
    
    unscrambled = []
    for byte in bytes_list:
        unscrambled.append(shift(byte))
    
    for i in range(len(unscrambled)):
        for j in range(i + 1, len(unscrambled)):
            unscrambled[j] = unshift(unscrambled[j])
    
    return unscrambled

# Example usage:
n = int(input())
bytes_list = list(map(int, input().split()))
unscrambled_bytes = unscramble(n, bytes_list)
for byte in unscrambled_bytes:
    print(byte, end=' ')