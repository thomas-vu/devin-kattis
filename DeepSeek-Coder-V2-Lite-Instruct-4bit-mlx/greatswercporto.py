def find_solutions(words, result):
    from itertools import permutations
    
    def is_valid_permutation(perm):
        letter_to_digit = {letter: digit for letter, digit in zip(distinct_letters, perm)}
        if any(letter_to_digit[word[0]] == 0 for word in words):
            return False
        sum_values = sum(int(''.join(str(letter_to_digit[c]) for c in word)) for word in words[:-1])
        return sum_values == int(''.join(str(letter_to_digit[c]) for c in result))
    
    distinct_letters = ''.join(set(''.join(words + [result])))
    max_len = len(max(words, key=len))
    
    solutions = 0
    for perm in permutations(range(10), len(distinct_letters)):
        if is_valid_permutation(perm):
            solutions += 1
    return solutions

n = int(input().strip())
words = [input().strip() for _ in range(n)]
solutions = find_solutions(words, words[-1])
print(solutions)