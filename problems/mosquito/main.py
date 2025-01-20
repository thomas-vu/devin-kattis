def calculate_mosquitos(M, P, L, E, R, S, N):
    for _ in range(N):
        new_larvae = M * E
        surviving_larvae = (new_larvae + L) // R
        new_pupae = surviving_larvae
        surviving_pupae = new_pupae // S
        M, P, L = 0, new_pupae, surviving_larvae
        M = surviving_pupae
    return P

def main():
    while True:
        try:
            M, P, L, E, R, S, N = map(int, input().split())
            result = calculate_mosquitos(M, P, L, E, R, S, N)
            print(result)
        except EOFError:
            break

if __name__ == "__main__":
    main()