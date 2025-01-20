import sys

def main():
    while True:
        line = input().strip()
        if line == "0 0 0":
            break
        r, m, c = map(float, line.split())
        true_area = 3.141592653589793 * r ** 2
        estimate_area = (c / m) * (r * 2) ** 2
        print(f"{true_area:.10f} {estimate_area:.10f}")

if __name__ == "__main__":
    main()