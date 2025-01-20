def count_digits(n):
    # The number of triangles doubles with each iteration, starting from 3.
    # After n iterations, the number of triangles is 3 * 2^n.
    # The circumference after n iterations is the number of triangles, which gives us 3 * 2^n.
    # We need to find the number of decimal digits required to represent this number.
    triangles = 3 * (2 ** n)
    
    # Find the number of decimal digits required to represent triangles.
    if triangles == 0:
        return 1
    digits = 0
    while triangles > 0:
        triangles //= 10
        digits += 1
    return digits

def main():
    case = 0
    while True:
        try:
            n = int(input())
            case += 1
            result = count_digits(n)
            print(f"Case {case}: {result}")
        except EOFError:
            break

if __name__ == "__main__":
    main()