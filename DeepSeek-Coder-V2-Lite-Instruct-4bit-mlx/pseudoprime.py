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

def is_base_a_pseudoprime(p, a):
    if not is_prime(p):
        return False
    return pow(a, p, p) == a

while True:
    line = input()
    if line == "0 0":
        break
    p, a = map(int, line.split())
    if is_base_a_pseudoprime(p, a):
        print("yes")
    else:
        print("no")