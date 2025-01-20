def calculate_raggedness(paragraph):
    lines = paragraph.split('\n')
    total_lengths = [len(line) for line in lines]
    
    max_line_length = max(total_lengths)
    raggedness_score = 0
    
    for i in range(len(total_lengths) - 1):
        n = max_line_length
        m = total_lengths[i]
        penalty = (n - m) ** 2
        raggedness_score += penalty
    
    return raggedness_score

paragraph = ""
while True:
    line = input()
    if not line:
        break
    paragraph += line + '\n'

print(calculate_raggedness(paragraph.strip()))