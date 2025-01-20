def main():
    Q = int(input())
    orders = [input().split() for _ in range(Q)]
    
    # Initialize the sequence of letters spoken
    sequence = ""
    reverse_mode = False
    
    for order in orders:
        command, param = order[0], order[1]
        
        if command == "SMJER":
            n = int(param)
            # Toggle reverse mode if the position is a multiple of 4
            reverse_mode = (n % 4 == 0)
            # Generate the sequence up to this position
            for i in range(1, n + 1):
                sequence += chr(ord('a') + (i - 1) % 26)
        elif command == "UPIT":
            n, x = int(param[:-1]), param[-1]
            count = sequence[:n].count(x) if not reverse_mode else sequence[:(n // 4 * 4)][::-1].count(x)
            print(count)

if __name__ == "__main__":
    main()