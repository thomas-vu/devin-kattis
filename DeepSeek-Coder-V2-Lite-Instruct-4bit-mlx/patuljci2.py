def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    C = int(data[index + 1])
    colors = list(map(int, data[index + 2: index + 2 + N]))
    M = int(data[index + 2 + N])
    
    pictures = []
    for i in range(M):
        A = int(data[index + 2 + N + i * 2]) - 1
        B = int(data[index + 2 + N + i * 2 + 1]) - 1
        pictures.append((A, B))
    
    for A, B in pictures:
        hat_counts = [0] * (C + 1)
        for j in range(A, B + 1):
            hat_counts[colors[j]] += 1
        dominating_color = hat_counts.index(max(hat_counts))
        if hat_counts[dominating_color] > (B - A + 1) // 2:
            print(f"yes {dominating_color}")
        else:
            print("no")

if __name__ == "__main__":
    main()