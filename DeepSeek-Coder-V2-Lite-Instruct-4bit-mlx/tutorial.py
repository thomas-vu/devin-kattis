def determine_result(m, n, t):
    if t == 1:
        return "AC" if n <= m else "TLE"
    elif t == 2:
        return "AC" if n <= m else "TLE"
    elif t == 3:
        return "AC" if n**4 <= m else "TLE"
    elif t == 4:
        return "AC" if n**3 <= m else "TLE"
    elif t == 5:
        return "AC" if n**2 <= m else "TLE"
    elif t == 6:
        return "AC" if n * (2 ** (n / 2)) <= m else "TLE"
    elif t == 7:
        return "AC" if n <= m else "TLE"

# Read input from stdin
m, n, t = map(int, input().split())
result = determine_result(m, n, t)
print(result)