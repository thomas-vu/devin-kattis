def is_in_mandelbrot(x, y, max_iterations):
    c = complex(x, y)
    z = 0 + 0j
    for i in range(max_iterations):
        z = z**2 + c
        if abs(z) > 2:
            return 'OUT'
    return 'IN'

def main():
    case_number = 1
    while True:
        try:
            x, y, r = map(float, input().split())
            result = is_in_mandelbrot(x, y, r)
            print(f'Case {case_number}: {result}')
            case_number += 1
        except EOFError:
            break

if __name__ == "__main__":
    main()