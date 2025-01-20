def can_form_digit(x, y):
    match_counts = {
        '0': 6, '1': 2, '2': 5, '3': 5, '4': 4,
        '5': 5, '6': 6, '7': 3, '8': 7, '9': 6
    }
    
    return match_counts[x] == match_counts[y] + 1

def main():
    X, Y = input().split()
    can_change = False
    
    for i in range(len(X)):
        if can_form_digit(X[i], Y[i]):
            can_change = True
            break
    
    print("yes" if can_change else "no")

if __name__ == "__main__":
    main()