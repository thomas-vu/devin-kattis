def extend_name(Y, P):
    if Y.endswith('e'):
        return Y + 'x' + P
    elif Y[-1] in 'aiou':
        return Y[:-1] + 'ex' + P
    elif Y.endswith('x'):
        return Y + P
    else:
        return Y + 'ex' + P

# Read input
Y, P = input().split()

# Output the extended name
print(extend_name(Y, P))