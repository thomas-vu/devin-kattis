def longest_loop(segments):
    blue = [seg for seg in segments if seg[1] == 'B']
    red = [seg for seg in segments if seg[1] == 'R']
    
    if not blue or not red:
        return 0
    
    blue.sort(reverse=True)
    red.sort(reverse=True)
    
    max_length = 0
    for i in range(min(len(blue), len(red))):
        max_length += blue[i][0] + red[i][0] - 1
    
    return max_length

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    index += 1
    results = []
    
    for _ in range(N):
        S = int(data[index])
        index += 1
        segments = []
        for i in range(S):
            length, color = data[index].split()
            segments.append((int(length), color))
            index += 1
        results.append(f"Case #{_+1}: {longest_loop(segments)}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()