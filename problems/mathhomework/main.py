def find_animals(b, d, c, l):
    solutions = []
    for birds in range(l // b + 1):
        for dogs in range(l // d + 1):
            for cats in range(l // c + 1):
                if birds * b + dogs * d + cats * c == l:
                    solutions.append((birds, dogs, cats))
    return solutions

def main():
    while True:
        try:
            b, d, c, l = map(int, input().split())
            solutions = find_animals(b, d, c, l)
            if not solutions:
                print("impossible")
            else:
                solutions = sorted(solutions, key=lambda x: (x[0], x[1], x[2]))
                for solution in solutions:
                    print(f"{solution[0]} {solution[1]} {solution[2]}")
        except EOFError:
            break

if __name__ == "__main__":
    main()