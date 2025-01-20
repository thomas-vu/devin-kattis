def is_golomb(marks):
    marks = sorted(marks)
    distances = set()
    for i in range(len(marks)):
        for j in range(i + 1, len(marks)):
            distance = marks[j] - marks[i]
            if distance in distances:
                return False, []
            distances.add(distance)
    max_distance = marks[-1]
    for i in range(1, max_distance):
        if i not in distances:
            return False, [i]
    return True, []

def main():
    while True:
        try:
            marks = list(map(int, input().split()))
            if len(marks) < 2:
                continue
            is_perfect, missing = is_golomb(marks)
            if is_perfect:
                print('perfect')
            elif missing:
                print(f'missing {" ".join(map(str, missing))}')
            else:
                print('not a ruler')
        except EOFError:
            break

if __name__ == "__main__":
    main()