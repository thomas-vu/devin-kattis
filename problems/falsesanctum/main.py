def calculate_density(s):
    density = 0
    i = 0
    while i < len(s):
        char_count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            char_count += 1
        density += char_count ** 2
        i += 1
    return density

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    Q = int(data[1])
    S = data[2]
    
    queries = []
    for i in range(Q):
        query_type, *params = data[i + 3].split()
        if query_type == '1':
            index = int(params[0]) - 1
            new_char = params[1]
            S = S[:index] + new_char + S[index+1:]
        elif query_type == '2':
            l = int(params[0]) - 1
            r = int(params[1]) - 1
            substring = S[l:r+1]
            density = calculate_density(substring)
            print(density)

if __name__ == "__main__":
    main()