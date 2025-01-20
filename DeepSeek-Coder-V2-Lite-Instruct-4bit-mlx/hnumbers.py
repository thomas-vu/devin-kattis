def is_h_number(n):
    return n % 4 == 1

def generate_h_numbers(limit):
    h_numbers = []
    for i in range(1, limit + 1):
        if is_h_number(i):
            h_numbers.append(i)
    return h_numbers

def generate_h_semi_primes(limit):
    h_numbers = generate_h_numbers(limit)
    h_semi_primes = set()
    
    for i in range(len(h_numbers)):
        for j in range(i, len(h_numbers)):
            product = h_numbers[i] * h_numbers[j]
            if product <= limit:
                h_semi_primes.add(product)
    
    return sorted(h_semi_primes)

def count_h_semi_primes(limit):
    h_numbers = generate_h_numbers(limit)
    h_semi_primes = set()
    
    for i in range(len(h_numbers)):
        for j in range(i, len(h_numbers)):
            product = h_numbers[i] * h_numbers[j]
            if product <= limit:
                h_semi_primes.add(product)
    
    return len(h_semi_primes)

def main():
    while True:
        h = int(input())
        if h == 0:
            break
        count = count_h_semi_primes(h)
        print(f"{h} {count}")

if __name__ == "__main__":
    main()