def find_palindromes(s):
    palindromes = set()
    n = len(s)
    
    # Check all possible substrings
    for i in range(n):
        for j in range(i + 2, n + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return sorted(palindromes)

def main():
    while True:
        try:
            s = input()
            palindromes = find_palindromes(s)
            for p in palindromes:
                print(p)
            print()
        except EOFError:
            break

if __name__ == "__main__":
    main()