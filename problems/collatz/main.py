def collatz_steps(x):
    steps = 0
    while x != 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
        steps += 1
    return steps

def main():
    while True:
        A, B = map(int, input().split())
        if A == 0 and B == 0:
            break
        SA = collatz_steps(A)
        SB = collatz_steps(B)
        while A != B:
            if A > B:
                A //= 2
            else:
                B //= 2
        C = A
        print(f"{A} needs {SA} steps, {B} needs {SB} steps, they meet at {C}")

if __name__ == "__main__":
    main()