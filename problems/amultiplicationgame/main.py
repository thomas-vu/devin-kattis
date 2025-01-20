def who_wins(n):
    if n == 1:
        return "Stan wins."
    
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            if n >= 9:
                n //= 9
            elif n >= 3:
                n //= 3
    
    return "Stan wins." if is_even(initial_n) else "Ollie wins."

def is_even(n):
    return n % 2 == 0

while True:
    try:
        n = int(input())
        print(who_wins(n))
    except EOFError:
        break