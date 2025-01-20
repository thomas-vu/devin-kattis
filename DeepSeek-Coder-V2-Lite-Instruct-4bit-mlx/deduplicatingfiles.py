def xor_hash(file_content):
    return ''.join(chr(ord(byte) ^ 0xFF if byte.isprintable() else ord(byte)) for byte in file_content)

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        
        files = [input().strip() for _ in range(n)]
        hashes = {}
        
        # Calculate the hash for each file and count collisions
        for file in files:
            h = xor_hash(file)
            if h not in hashes:
                hashes[h] = []
            hashes[h].append(file)
        
        unique_files = 0
        collisions = 0
        
        # Count the number of unique files and collisions
        for hash_value, file_list in hashes.items():
            if len(file_list) > 1:
                unique_files += 1
                collisions += len(file_list) - 1
        
        print(len(hashes), collisions)

if __name__ == "__main__":
    main()