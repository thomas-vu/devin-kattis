def translate_sentence(N, sentence, M, dictionary):
    translation_dict = {pair[0]: pair[1] for pair in dictionary}
    words = sentence.split()
    translated_words = [translation_dict[word] if word in translation_dict else word for word in words]
    return ' '.join(translated_words)

# Read input
N = int(input())
sentence = input()
M = int(input())
dictionary = [tuple(input().split()) for _ in range(M)]

# Translate and print the sentence
translated_sentence = translate_sentence(N, sentence, M, dictionary)
print(translated_sentence)