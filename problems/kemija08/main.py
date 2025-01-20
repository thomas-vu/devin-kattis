import re

def decode_sentence(coded_sentence):
    def decode_word(word):
        return re.sub(r'(.)p\1', r'\1', word)
    
    words = coded_sentence.split()
    decoded_words = [decode_word(word) for word in words]
    return ' '.join(decoded_words)

# Read input from stdin
coded_sentence = input()
decoded_sentence = decode_sentence(coded_sentence)
print(decoded_sentence)