def find_darts(n):
    for a in range(21):
        for b in range(21):
            for c in range(21):
                if a*3 + b*2 + c*1 == n:
                    return f"triple {a}\ndouble {b}\nsingle {c}"
    return "impossible"

# Read the input
n = int(input())

# Output the result
print(find_darts(n))