def count_syllables(poem, syllables):
    word_list = poem.split()
    syllable_count = 0
    for word in word_list:
        if word in syllables:
            syllable_count += 1
    return syllable_count

def is_haiku(syllables, poem):
    phrases = poem.split('\n')
    phrase_counts = [5, 7, 5]
    
    for i in range(3):
        phrase_syllables = phrases[i].split()
        syllable_count = sum(count_syllables(word, syllables) for word in phrase_syllables)
        if syllable_count != phrase_counts[i]:
            return "come back next year"
    return "haiku"

# Read input
S = int(input())
syllables_str = input().split()
poem = ""
for _ in range(3):
    poem += input() + "\n"

# Output the result
print(is_haiku(syllables_str, poem.strip()))