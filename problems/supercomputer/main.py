def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    K = int(data[index + 1])
    index += 2
    
    memory = [0] * N
    
    for _ in range(K):
        query = data[index]
        index += 1
        
        if query == 'F':
            i = int(data[index]) - 1
            memory[i] ^= 1
        elif query == 'C':
            l = int(data[index]) - 1
            r = int(data[index + 1]) - 1
            count = sum(memory[l:r+1])
            print(count)
            index += 2

if __name__ == "__main__":
    main()