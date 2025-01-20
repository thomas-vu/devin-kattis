def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def find_minimal_p(N):
    p = 11
    while True:
        if sum_of_digits(N * p) == sum_of_digits(N):
            return p
        p += 1

while True:
    N = int(input())
    if N == 0:
        break
    p = find_minimal_p(N)
    print(p)