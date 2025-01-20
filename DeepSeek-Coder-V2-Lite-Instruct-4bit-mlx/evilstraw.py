def min_swaps_to_palindrome(s):
    n = len(s)
    if not can_form_palindrome(s):
        return "Impossible"
    
    swaps = 0
    for i in range(n // 2):
        left, right = i, n - i - 1
        while left < right:
            if s[left] == s[right]:
                break
            else:
                right -= 1
        if left == right:
            # The character at the middle needs to be swapped with some other character
            s = swap(s, left, left + 1)
            swaps += 1
        else:
            for j in range(right, n - i - 1):
                s = swap(s, j, j + 1)
                swaps += 1
    return swaps

def can_form_palindrome(s):
    char_count = [0] * 26
    for c in s:
        char_count[ord(c) - ord('a')] += 1
    odd_count = sum(1 for i in char_count if i % 2 == 1)
    return odd_count <= 1

def swap(s, i, j):
    s_list = list(s)
    s_list[i], s_list[j] = s_list[j], s_list[i]
    return ''.join(s_list)

# Read number of test cases
t = int(input().strip())
for _ in range(t):
    s = input().strip()
    print(min_swaps_to_palindrome(s))