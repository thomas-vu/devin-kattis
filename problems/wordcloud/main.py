def calculate_font_size(cw, cmax):
    return 8 + int((40 * (cw - 4)) / (cmax - 4))

def calculate_word_width(t, P):
    return int((9 / 16) * t * P + 0.5)

def generate_word_cloud(W, words):
    word_heights = {}
    max_count = max([word[1] for word in words])
    
    for word, count in words:
        font_size = calculate_font_size(count, max_count)
        word_width = calculate_word_width(len(word), font_size)
        while word_width > W:
            font_size -= 1
            word_width = calculate_word_width(len(word), font_size)
        if word not in word_heights:
            word_heights[word] = font_size
    
    sorted_words = sorted(words, key=lambda x: (x[0], -x[1]))
    cloud_height = 0
    current_row_width = 0
    max_font_size_in_row = 0
    
    for word, count in sorted_words:
        font_size = word_heights[word]
        word_width = calculate_word_width(len(word), font_size)
        
        if current_row_width + word_width + (10 if current_row_width > 0 else 0) <= W:
            current_row_width += word_width + 10
            max_font_size_in_row = max(max_font_size_in_row, font_size)
        else:
            cloud_height += max_font_size_in_row
            current_row_width = word_width + 10
            max_font_size_in_row = font_size
    
    cloud_height += max_font_size_in_row
    return cloud_height

def main():
    T = 0
    while True:
        W, N = map(int, input().split())
        if W == 0 and N == 0:
            break
        T += 1
        words = []
        for _ in range(N):
            word, count = input().split()
            words.append((word, int(count)))
        height = generate_word_cloud(W, words)
        print(f"CLOUD {T}: {height}")

if __name__ == "__main__":
    main()