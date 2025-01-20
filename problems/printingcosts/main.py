# Solution to the toner cost problem

costs = [0, 9, 6, 24, 29, 22, 24, 3, 12, 12, 17, 13, 7, 7, 4, 10, 22, 19, 22, 23, 21, 27, 26, 16, 23, 26, 26, 20, 25, 25, 18, 18, 21, 16, 28, 25, 26, 23, 31, 28, 25, 25, 13, 21, 17, 17, 13, 19, 13, 24, 10, 19, 15, 28, 21, 16, 14, 22, 32, 24, 29, 20, 26, 26, 20, 25, 25, 18, 30, 21, 15, 20, 21, 16, 22, 18, 10, 3, 25, 25, 17, 25, 23, 18, 25, 18, 7, 8, 10, 18, 7, 4, 32, 24, 29, 20, 26, 23, 18, 19, 13, 19, 12, 18, 7, 8, 31, 9]

def calculate_toner(line):
    total_cost = 0
    for char in line:
        if ord(char) >= 32 and ord(char) <= 126:
            total_cost += costs[ord(char) - 31]
    return total_cost

while True:
    try:
        line = input()
        print(calculate_toner(line))
    except EOFError:
        break