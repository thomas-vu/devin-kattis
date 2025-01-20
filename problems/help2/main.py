def match_patterns(pattern1, pattern2):
    words1 = pattern1.split()
    words2 = pattern2.split()
    
    # Create a mapping for each word in the first pattern to words in the second pattern
    map1 = {}
    map2 = {}
    
    for w1, w2 in zip(words1, words2):
        if w1 not in map1:
            map1[w1] = set()
        if w2 not in map2:
            map2[w2] = set()
        map1[w1].add(w2)
        map2[w2].add(w1)
    
    # Check for consistency in mappings
    for key in map1:
        if len(map1[key]) != 1 or len(map2[key]) != 1:
            return "-"
    
    # Create the matching phrase
    result = []
    for w1, w2 in zip(words1, words2):
        mapped_word = list(map1[w1])[0]
        result.append(mapped_word)
    
    return ' '.join(result)

n = int(input())
for _ in range(n):
    pattern1 = input()
    pattern2 = input()
    print(match_patterns(pattern1, pattern2))