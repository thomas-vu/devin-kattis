def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def check_output(line):
    parts = line.split()
    if len(parts) != 3:
        return False
    try:
        even_number = int(parts[0])
        if even_number <= 3 or even_number % 2 != 0:
            return False
        prime1 = int(parts[1])
        prime2 = int(parts[2])
        if not is_prime(prime1) or not is_prime(prime2):
            return False
        if prime1 + prime2 != even_number:
            return False
    except (ValueError, IndexError):
        return False
    return True

def main():
    while True:
        try:
            line = input()
        except EOFError:
            break
        if check_output(line):
            print(1)
        else:
            print(0)

if __name__ == "__main__":
    main()