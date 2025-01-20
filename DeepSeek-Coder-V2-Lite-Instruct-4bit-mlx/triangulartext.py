def print_triangular_text(text):
    words = text.split()
    max_width = len(words)
    min_spaces = 0
    
    while max_width > min_spaces:
        for i in range(max_width - min_spaces):
            print(" ".join(words[i:]))
        min_spaces += 1
        
# Sample Input
input_text = "MUCH CURRENT RESEARCH IN ARTIFICIAL INTELLIGENCE INVOLVES DESIGNING PROGRAMS THAT CAPTURE THE KNOWLEDGE AND REASONING PROCESS OF HIGHLY INTELLIGENT SPECIALISTS.  THE PRACTICAL GOAL OF SUCH WORK IS TO MAKE SPECIALIZED EXPERTISE MORE GENERALLY ACCESSIBLE."

# Output the result in triangular format
print_triangular_text(input_text)