def is_true_canadian(sentence):
    return sentence.endswith('eh?')

# Read input from stdin
sentence = input().strip()

# Determine if the speaker is a true Canadian or an imposter
if is_true_canadian(sentence):
    print("Canadian!")
else:
    print("Imposter!")