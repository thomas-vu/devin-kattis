def find_closest_smaller(N):
    sum_digits = sum(int(digit) for digit in str(N))
    closest_smaller = N - 1
    
    while sum(int(digit) for digit in str(closest_smaller)) != sum_digits - 1:
        closest_smaller -= 1
    
    return closest_smaller

def main():
    T = int(input())
    results = []
    
    for _ in range(T):
        N = int(input())
        results.append(find_closest_smaller(N))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()