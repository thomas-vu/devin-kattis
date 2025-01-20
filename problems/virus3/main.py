F = input().strip()
H = input().strip()

# Check if H could be formed by adding exactly one character to F
def is_possible_transformation(F, H):
    if len(H) == len(F) + 1:
        for i in range(len(F)):
            if F[i] != H[i]:
                return F[:i] + H[i:] == H
        return True  # Last character of F is the missing one in H
    elif len(H) == len(F):
        diff_count = 0
        for i in range(len(F)):
            if F[i] != H[i]:
                diff_count += 1
                if diff_count > 1:
                    return False
        return True  # Only one character is different or the same
    else:
        return False

if is_possible_transformation(F, H):
    print("Ja")
else:
    print("Nej")