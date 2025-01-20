def find_king(gnome_ids):
    for i in range(1, len(gnome_ids)):
        if gnome_ids[i] != gnome_ids[i-1] + 1:
            return i + 1
    return -1

def main():
    n = int(input())
    for _ in range(n):
        line = list(map(int, input().split()))
        g = line[0]
        gnome_ids = line[1:]
        king_position = find_king(gnome_ids)
        print(king_position)

if __name__ == "__main__":
    main()