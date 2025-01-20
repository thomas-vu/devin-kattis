def is_valid_siteswap(pattern):
    throws = list(map(int, pattern))
    total_throws = sum(throws)
    num_beats = len(throws)
    
    if total_throws % num_beats != 0:
        return "invalid # of balls"
    
    hands = [0, 0]  # left hand, right hand
    
    for i in range(len(throws)):
        if throws[i] == 0:
            continue
        beat = i % num_beats
        if throws[i] > 0:
            hand = beat % 2
            hands[hand] += throws[i]
        else:
            hand = (beat + 1) % 2
            hands[hand] += abs(throws[i])
    
    if any(hands[0] > (num_beats // 2) or hands[1] > (num_beats // 2)):
        return "invalid pattern"
    
    return f"valid with {num_beats // 2} balls"

def main():
    while True:
        try:
            pattern = input().strip()
            result = is_valid_siteswap(pattern)
            print(f"{pattern}: {result}")
        except EOFError:
            break

if __name__ == "__main__":
    main()