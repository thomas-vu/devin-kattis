def game_outcome(a, b):
    while a != 0 and b != 0:
        if a < b:
            a, b = b, a
        if a >= 2 * b:
            return "Stan wins"
        a %= b
    return "Ollie wins" if a == 0 else "Stan wins"

def main():
    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        print(game_outcome(a, b))

if __name__ == "__main__":
    main()