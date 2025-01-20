def largest_product(n):
    MOD = 1000000007
    max_square = int(n**0.5) + 1
    largest_d = 0
    
    for i in range(2, max_square):
        product = 1
        num = i
        while num <= n and product * num <= n:
            product *= num
            if largest_d < product:
                largest_d = product
            num += 1
    
    return largest_d % MOD

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        print(largest_product(n))

if __name__ == "__main__":
    main()