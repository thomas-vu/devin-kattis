def find_gold_stack(w, s):
    c = (s * (s + 1)) // 2
    expected_weight = 29260 * c + (w - 29260 * s)
    gold_stack = (expected_weight - w) // (29370 - 29260)
    return gold_stack + 1

# Read input from stdin
w, s = map(int, input().split())
print(find_gold_stack(w, s))