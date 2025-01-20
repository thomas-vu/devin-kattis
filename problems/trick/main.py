import sys

def main():
    X = float(sys.stdin.readline().strip())
    results = []
    
    for n in range(1, 10**8):
        str_n = str(n)
        if len(str_n) > 8:
            break
        new_number = int(str_n[1:] + str_n[0])
        if new_number == X * n:
            results.append(n)
    
    if results:
        for result in results:
            print(result)
    else:
        print("No solution")

if __name__ == "__main__":
    main()