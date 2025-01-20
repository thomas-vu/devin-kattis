def rotate_and_cut(sentence, N):
    def rotate(s):
        return s[::-1]
    
    for _ in range(N):
        sentence = rotate(sentence)
        cut_length = len(sentence) // 4
        sentence = sentence[:-cut_length] if cut_length > 0 else sentence
    return sentence

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    num_cases = int(data[0])
    results = []
    
    for i in range(1, num_cases + 1):
        N = int(data[i].split()[0])
        sentence = data[i].split()[1]
        result = rotate_and_cut(sentence, N)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()