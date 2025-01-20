def find_visually_appealing_flags(S):
    def generate_patterns(stars, first_row, second_row):
        if stars == 0:
            return [[]]
        patterns = []
        for i in range(first_row, min(S - (second_row - 1), S) + 1):
            for j in range(max(second_row, i - 1), min(S - (first_row - 1), S) + 1):
                if i != j:
                    for pattern in generate_patterns(stars - i, i, j):
                        patterns.append([f"{i},{j}"] + pattern)
        return patterns

    results = generate_patterns(S, 1, 0)
    results.sort(key=lambda x: (int(x[0].split(',')[0]), int(x[0].split(',')[1])))
    compact_representations = [f"{int(row.split(',')[0])},{int(row.split(',')[1])}" for row in results[0]]
    return compact_representations

def main():
    S = int(input().strip())
    if S <= 3:
        print("{}:".format(S))
    else:
        compact_representations = find_visually_appealing_flags(S)
        print("{}:".format(S))
        for representation in compact_representations:
            print(representation)

if __name__ == "__main__":
    main()