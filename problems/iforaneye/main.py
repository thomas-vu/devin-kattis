def abbreviate(word):
    replacements = {
        'at': '@',
        'and': '&',
        'one': '1',
        'two': '2',
        'four': '4',
        'bea': 'b',
        'see': 'c',
        'eye': 'e',
        'oh': 'o'
    }
    
    for original, replacement in replacements.items():
        if original.lower() == word:
            return replacement
        elif original.upper() == word:
            return replacement.upper()
        else:
            index = word.find(original)
            while index != -1:
                if index == 0 or not word[index-1].isalnum():
                    if index + len(original) == len(word) or not word[index+len(original)].isalnum():
                        new_word = word[:index] + replacement + word[index+len(original):]
                        return new_word
                index = word.find(original, index + 1)
    return word

def process_line(line):
    words = line.split()
    new_words = [abbreviate(word) for word in words]
    return ' '.join(new_words)

n = int(input())
lines = [input() for _ in range(n)]
for line in lines:
    print(process_line(line))