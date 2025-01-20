def can_win(xor_sum, allowed_moves):
    if xor_sum == 0:
        return False
    for move in allowed_moves:
        if xor_sum & move != 0 and not can_win(xor_sum ^ move, allowed_moves):
            return True
    return False

def main():
    while True:
        try:
            allowed_moves = list(map(int, input().split()))[1:]
            num_positions = int(input())
            for _ in range(num_positions):
                heaps = list(map(int, input().split()))[1:]
                xor_sum = 0
                for heap in heaps:
                    xor_sum ^= heap
                if can_win(xor_sum, allowed_moves):
                    print('W')
                else:
                    print('L')
        except EOFError:
            break

if __name__ == "__main__":
    main()