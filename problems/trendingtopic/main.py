from collections import defaultdict, Counter
import re

class TrendingTopics:
    def __init__(self):
        self.word_count = defaultdict(int)
        self.day_words = []
        self.top_n = 0

    def process_text(self, text):
        words = re.findall(r'\b[a-z]{4,20}\b', text)
        for word in words:
            self.word_count[word] += 1
        self.day_words.append(self.word_count.copy())
        self.word_count.clear()

    def process_query(self, query):
        top_n = int(query.split()[1])
        self.top_n = top_n
        word_freqs = defaultdict(int)
        for day in self.day_words:
            for word, freq in day.items():
                word_freqs[word] += freq
        sorted_words = sorted(word_freqs.items(), key=lambda x: (-x[1], x[0]))
        result = [word for word, freq in sorted_words if freq == sorted_words[top_n - 1][1]]
        result.sort()
        return result[:top_n]

# Main processing loop
trending = TrendingTopics()
while True:
    try:
        line = input().strip()
        if line.startswith("<text>"):
            text = ""
            while True:
                next_line = input().strip()
                if next_line.startswith("</text>"):
                    text += " " + next_line[6:]
                    trending.process_text(text)
                    break
                text += " " + next_line
        elif line.startswith("<top"):
            query = input().strip()
            result = trending.process_query(query)
            for word in result:
                print(word)
    except EOFError:
        break