def count_rotated_pairs(A, B):
    def is_valid_pair(n, m):
        str_n = str(n)
        for i in range(len(str_n)):
            rotated = str_n[i:] + str_n[:i]
            if int(rotated) == m and set(str_n) == set(rotated):
                return True
        return False
    
    count = 0
    for n in range(A, B):
        for m in range(n + 1, B + 1):
            if is_valid_pair(n, m):
                count += 1
    return count

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    num_datasets = int(data[0])
    results = []
    
    for i in range(1, num_datasets + 1):
        A = int(data[i].split()[0])
        B = int(data[i].split()[1])
        results.append(count_rotated_pairs(A, B))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()