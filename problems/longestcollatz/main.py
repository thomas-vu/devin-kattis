def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

def find_max_steps(n):
    max_steps = 0
    number_with_max_steps = 0
    for i in range(1, n):
        steps = collatz_steps(i)
        if steps > max_steps:
            max_steps = steps
            number_with_max_steps = i
    return number_with_max_steps

n = int(input())
print(find_max_steps(n))