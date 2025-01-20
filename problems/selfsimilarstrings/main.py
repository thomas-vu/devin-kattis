def largest_degree_of_self_similarity(s):
    n = len(s)
    for d in range(n-1, -1, -1):
        found = True
        for i in range(n-d):
            if s[i:i+d+1] not in s[i+1:]:
                found = False
                break
        if found:
            return d+1
    return 0

def main():
    while True:
        try:
            s = input().strip()
            if not s:
                continue
            print(largest_degree_of_self_similarity(s))
        except EOFError:
            break

if __name__ == "__main__":
    main()