def main():
    n, q = map(int, input().split())
    names = []
    for _ in range(n):
        first_name, last_name = input().split()
        names.append((first_name[0] + last_name[0], first_name + ' ' + last_name))
    
    queries = [input().strip() for _ in range(q)]
    
    for query in queries:
        matching_names = [name for name, full_name in names if query == (full_name.split()[0][0] + full_name.split()[1][0])]
        if len(matching_names) == 1:
            print(matching_names[0].split()[0] + ' ' + matching_names[0].split()[1])
        elif len(matching_names) > 1:
            print('ambiguous')
        else:
            print('nobody')

if __name__ == "__main__":
    main()