from collections import Counter, defaultdict
import sys

def main():
    while True:
        line = input().strip()
        if not line:  # Break on empty line
            break
        
        words = [word.upper() for word in line.split()]
        word_counts = defaultdict(int)
        
        for word in words:
            word_counts[word] += 1
        
        most_common_count = max(word_counts.values())
        current_length = 1
        
        while most_common_count > 1:
            filtered_words = [word for word in words if len(word) == current_length]
            filtered_counts = Counter(filtered_words)
            most_common_count = max(filtered_counts.values())
            
            if most_common_count > 1:
                print(most_common_count)
            
            current_length += 1
        
        print()

if __name__ == "__main__":
    main()