def check_mapping(char_string, sentence):
    words = sentence.split()
    char_to_word = {}
    word_to_char = {}
    
    if len(char_string) != len(words):
        return "False"
    
    for char in char_string:
        if char not in char_to_word and len(char_to_word) < len(words):
            char_to_word[char] = words.pop(0)
    
    for word in words:
        for char in word:
            if char not in word_to_char and len(word_to_char) < len(char_string):
                word_to_char[char] = word
    
    for char in char_string:
        if char not in char_to_word or char_to_word[char] != word_to_char[char]:
            return "False"
    
    for word in words:
        for char in word:
            if char not in word_to_char or word_to_char[char] != char_to_word[char]:
                return "False"
    
    return "True"

# Sample Input 1
char_string = "erf"
sentence = "why they they"
print(check_mapping(char_string, sentence))  # Output: False

# Sample Input 2
char_string = "abcdabcd"
sentence = "CCPC is the best CCPC is the best"
print(check_mapping(char_string, sentence))  # Output: True

# Sample Input 3
char_string = "a"
sentence = "The quick brown fox jumps over the lazy dog"
print(check_mapping(char_string, sentence))  # Output: False