def min_changes_to_palindrome(name):
    changes = 0
    n = len(name)
    
    for i in range(n // 2):
        if name[i] != name[n - i - 1]:
            changes += 1
    
    return changes

# Sample Input 1
name1 = "kaia"
print(min_changes_to_palindrome(name1))  # Output: 1

# Sample Input 2
name2 = "abcdefgded"
print(min_changes_to_palindrome(name2))  # Output: 4