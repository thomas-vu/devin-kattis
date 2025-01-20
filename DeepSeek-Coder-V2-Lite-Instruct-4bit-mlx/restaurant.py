def process_commands(N, commands):
    piles = [[] for _ in range(2)]
    output = []
    
    for command in commands:
        action, num_str = command.split()
        m = int(num_str)
        
        if action == 'DROP':
            piles[0].append(m)
            output.append(f"DROP 1 {m}")
        elif action == 'TAKE':
            taken = 0
            while piles[0] and taken < m:
                plate = piles[0].pop(0)
                output.append(f"TAKE 1 {plate}")
                taken += plate
            if piles[0]:
                output.append(f"MOVE 1->2 {taken}")
                piles[1].extend([plate for plate in piles[0] if plate <= m - taken])
                plates_to_move = [plate for plate in piles[0] if plate > m - taken]
                piles[0] = plates_to_move
            else:
                for _ in range(m - taken):
                    plate = piles[1].pop(0)
                    output.append(f"TAKE 2 {plate}")
        elif action == 'MOVE':
            while piles[1] and m > 0:
                plate = piles[1].pop(0)
                output.append(f"MOVE 2->1 {plate}")
                piles[0].append(plate)
                m -= plate
        else:
            raise ValueError("Unknown action")
    
    return output

def main():
    while True:
        N = int(input())
        if N == 0:
            break
        commands = [input().strip() for _ in range(N)]
        output_commands = process_commands(N, commands)
        for command in output_commands:
            print(command)
        if N > 0:
            print()

if __name__ == "__main__":
    main()