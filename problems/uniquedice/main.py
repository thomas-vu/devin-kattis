def find_largest_set(dice):
    def rotate(faces):
        return [faces[0], faces[5], faces[1], faces[3], faces[2], faces[4]]
    
    def match(d1, d2):
        for _ in range(4):
            if (d1[0] == d2[0] and d1[5] == d2[5]) or \
               (d1[0] == d2[5] and d1[5] == d2[0]) or \
               (d1[1] == d2[1] and d1[3] == d2[3]) or \
               (d1[1] == d2[3] and d1[3] == d2[1]) or \
               (d1[2] == d2[2] and d1[4] == d2[4]) or \
               (d1[2] == d2[4] and d1[4] == d2[2]):
                return True
            d2 = rotate(d2)
        return False
    
    n = len(dice)
    max_set = 0
    
    for i in range(n):
        current_dice = [dice[i]]
        for j in range(n):
            if i != j and match(dice[i], dice[j]):
                current_dice.append(dice[j])
        max_set = max(max_set, len(current_dice))
    
    return max_set

# Read input
n = int(input())
dice = []
for _ in range(n):
    faces = list(map(int, input().split()))
    dice.append(faces)

# Output the result
print(find_largest_set(dice))