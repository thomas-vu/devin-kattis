def longest_common_sequence(s, i, j):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    max_length = 0
    for k in range(2):
        left, right = i, j
        if k == 1:
            left, right = j, i
        max_length = max(max_length, expand_around_center(left, right))
    
    return max_length

def main():
    s = input().strip()
    q = int(input().strip())
    for _ in range(q):
        i, j = map(int, input().strip().split())
        print(longest_common_sequence(s, i, j))

if __name__ == "__main__":
    main()