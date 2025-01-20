def check_number(N):
    is_odd = N % 2 != 0
    sqrt_N = int(N**0.5)
    is_perfect_square = sqrt_N * sqrt_N == N
    
    if is_odd and is_perfect_square:
        return 'OS'
    elif is_odd:
        return 'O'
    elif is_perfect_square:
        return 'S'
    else:
        return 'EMPTY'

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(check_number(N))

if __name__ == "__main__":
    main()