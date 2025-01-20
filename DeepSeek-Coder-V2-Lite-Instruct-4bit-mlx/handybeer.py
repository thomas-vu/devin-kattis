def min_time_to_type(t, s, text):
    left_hand = 'qwertasdfgzxcvb'
    right_hand = 'yuiophjklnm'
    
    def time_to_type(char, left_hand, right_hand):
        if char in left_hand:
            return t
        elif char in right_hand:
            return t
        else:  # space, comma, period
            return t
    
    def swap_time():
        return s
    
    n = len(text)
    total_time = 0
    for i in range(n):
        if text[i] in left_hand:
            total_time += time_to_type(text[i], left_hand, right_hand)
        elif text[i] in right_hand:
            total_time += time_to_type(text[i], left_hand, right_hand)
        else:  # space, comma, period
            total_time += time_to_type(text[i], left_hand, right_hand)
        
        if i < n - 1:
            left_char = text[i] in left_hand
            next_char = text[i + 1] in right_hand
            if left_char != next_char:
                total_time += swap_time()
    
    return total_time

# Read input
t, s = map(int, input().split())
text = input()

# Calculate and output the result
print(min_time_to_type(t, s, text))