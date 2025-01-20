def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def can_be_arranged(children):
    for i in range(len(children) - 1):
        if gcd(children[i], children[i + 1]) == 1:
            return False
    return True

def rearrange_children(children):
    if can_be_arranged(children):
        return children
    else:
        for i in range(len(children)):
            for j in range(i + 1, len(children)):
                if gcd(children[i], children[j]) > 1:
                    children[i], children[j] = children[j], children[i]
                    if can_be_arranged(children):
                        return children
                    else:
                        children[i], children[j] = children[j], children[i]
    return "Neibb"

# Read input
n = int(input())
children = list(map(int, input().split()))

# Rearrange children and print the result
result = rearrange_children(children)
print(" ".join(map(str, result)))