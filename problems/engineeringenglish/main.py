seen = set()
for line in iter(input, ""):
    words = [word.lower() for word in line.split()]
    new_line = []
    for word in words:
        if word not in seen:
            new_line.append(word)
            seen.add(word)
        else:
            new_line.append('.')
    print(' '.join(new_line))