def count_palindromic_substrings(s, l, r):
    count = 0
    for i in range(l - 1, r):
        for j in range(i + 1, r + 1):
            if s[i:j] == s[i:j][::-1]:
                count += 1
    return count

def main():
    s = input().strip()
    m = int(input().strip())
    
    for _ in range(m):
        l, r = map(int, input().strip().split())
        print(count_palindromic_substrings(s, l, r))

if __name__ == "__main__":
    main()