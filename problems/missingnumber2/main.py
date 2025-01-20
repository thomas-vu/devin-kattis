def find_missing_number(s):
    n = len(s)
    for length in range(1, min(n, 6)):
        a = int(s[:length])
        b = ""
        i = length
        while i < n:
            if s[i] == '0':
                break
            b += s[i]
            if int(b) > a and int(b) <= 99999:
                yield int(b)
            i += 1
        if b and int(b) > a and int(b) <= 99999:
            yield int(b)

t = int(input())
for _ in range(t):
    s = input()
    missing_numbers = []
    for num in find_missing_number(s):
        missing_numbers.append(num)
    print(len(missing_numbers))
    if missing_numbers:
        print(" ".join(map(str, sorted(missing_numbers))))