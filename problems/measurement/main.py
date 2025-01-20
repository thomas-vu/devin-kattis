conversion_factors = {
    'thou': 1,
    'inch': 1000,
    'foot': 12 * 1000,
    'yard': 3 * 12 * 1000,
    'chain': 22 * 3 * 12 * 1000,
    'furlong': 10 * 22 * 3 * 12 * 1000,
    'mile': 8 * 10 * 22 * 3 * 12 * 1000,
    'league': 3 * 8 * 10 * 22 * 3 * 12 * 1000
}

def convert_distance(v, u, new_u):
    factor_u = conversion_factors[u]
    factor_new_u = conversion_factors[new_u]
    return v * (factor_u / factor_new_u)

while True:
    try:
        v, u, _, new_u = input().split()
        v = int(v)
        print("{:.12f}".format(convert_distance(v, u, new_u)))
    except EOFError:
        break