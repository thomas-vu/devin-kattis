def count_possible_words(dictionary, key_presses):
    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def word_from_key_presses(word, key_presses):
        if not word:
            return True
        for digit in key_presses:
            if word[0] in mapping[digit]:
                word = word[1:]
            else:
                return False
        return True
    
    count = 0
    for word in dictionary:
        if word_from_key_presses(word, key_presses):
            count += 1
    return count

# Read input
N = int(input())
dictionary = [input() for _ in range(N)]
key_presses = input()

# Count and output the number of possible words
print(count_possible_words(dictionary, key_presses))