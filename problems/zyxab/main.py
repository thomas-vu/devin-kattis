def is_valid_name(name):
    return len(set(name)) == len(name) and 'a' in name and 'b' in name

def find_best_name(names):
    best_name = None
    for name in names:
        if len(name) >= 5 and is_valid_name(name):
            if best_name is None or len(name) < len(best_name) or (len(name) == len(best_name) and name > best_name):
                best_name = name
    return best_name if best_name else "Neibb"

n = int(input())
names = [input() for _ in range(n)]
print(find_best_name(names))