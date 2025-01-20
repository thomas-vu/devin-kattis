def find_available_name(used_names, x):
    i = 1
    while f"c_{x*i}" in used_names:
        i += 1
    return f"c_{x*i}"

def main():
    N = int(input())
    used_names = set()
    
    for _ in range(N):
        x = int(input())
        available_name = find_available_name(used_names, x)
        used_names.add(available_name)
        print(available_name)

if __name__ == "__main__":
    main()