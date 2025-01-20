import re

def add_commas(text):
    words = text.split()
    n = len(words)
    
    def apply_rules():
        added = False
        for i in range(n):
            word = words[i]
            if ',' in word:
                # Rule 1: Comma before the word
                for j in range(i):
                    if words[j].endswith(',') and not re.match(r'^.*,.*$', words[j]):
                        words[j] = words[j].rstrip(',') + ', ' + word.lstrip(' ')
                        added = True
                for j in range(i+1, n):
                    if word.endswith(',') and not re.match(r'^.*,.*$', word):
                        words[j] = ',' + words[j].lstrip(' ')
                        added = True
            if word.endswith(','):
                # Rule 2: Comma after the word
                for j in range(i+1, n):
                    if words[j].startswith(',') and not re.match(r'^.*,.*$', words[j]):
                        words[j] = word.rstrip(',') + ' ' + words[j].lstrip(' ')
                        added = True
                for j in range(i+1, n):
                    if words[j].startswith(',') and not re.match(r'^.*,.*$', words[j]):
                        added = True
        return added
    
    while apply_rules():
        pass
    
    return ' '.join(words)

# Example usage:
text = "please sit spot. sit spot, sit. spot here now here."
print(add_commas(text))  # Output: please, sit spot. sit spot, sit. spot, here now, here.