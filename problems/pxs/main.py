def find_subfactors(n):
    def is_subfactor(sub, fact):
        sub = str(sub)
        fact = str(fact)
        i, j = 0, 0
        while i < len(sub) and j < len(fact):
            if sub[i] == fact[j]:
                i += 1
            j += 1
        return i == len(sub)

    def generate_series(n):
        series = []
        while n > 1:
            subfactors = [x for x in range(2, int(n) + 1) if n % x == 0 and is_subfactor(x, n)]
            subfactors = [str(x) for x in subfactors if str(x)[0] != '0']
            min_subfactor = None
            for sub in subfactors:
                if not any(is_subfactor(str(sub), str(x)) for x in series):
                    min_subfactor = sub
                    break
            if min_subfactor is None:
                break
            series.append(int(min_subfactor))
            n = int(''.join([d for d in str(n) if d not in min_subfactor]))
        return series[::-1]

    n = int(n)
    if n == 0:
        return []
    series = generate_series(n)
    if not series:
        return [str(n)]
    return [str(x) for x in series]

def main():
    while True:
        line = input().strip()
        if line == '0':
            break
        print(' '.join(find_subfactors(line)))

if __name__ == "__main__":
    main()