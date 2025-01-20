def is_perfect(n):
    sum_divisors = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
    return sum_divisors == n

def is_almost_perfect(n):
    sum_divisors = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
    return abs(sum_divisors - n) <= 2

def classify_number(n):
    if is_perfect(n):
        return "perfect"
    elif is_almost_perfect(n):
        return "almost perfect"
    else:
        return "not perfect"

while True:
    try:
        p = int(input())
        result = classify_number(p)
        print(f"{p} {result}")
    except EOFError:
        break