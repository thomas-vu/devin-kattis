def min_moves_to_convert(S, T):
    if S == T:
        return 0
    
    # Check if transformation is possible
    for i in range(len(S)):
        if S[i] == '?':
            if T[i] == '0' and (i == 0 or S[i-1] != '1'):
                S = S[:i] + '0' + S[i+1:]
            elif T[i] == '1' and (i == 0 or S[i-1] != '0'):
                S = S[:i] + '1' + S[i+1:]
    
    # Count the number of differences
    diff_count = sum(1 for i in range(len(S)) if S[i] != T[i])
    
    # Check for the case where the transformation is impossible
    if S != T:
        return -1
    
    # Count the number of '?' in S
    question_marks = S.count('?')
    
    # Calculate the minimum number of moves
    min_moves = diff_count + question_marks
    
    return min_moves

def main():
    C = int(input())
    for case in range(1, C + 1):
        S = input()
        T = input()
        result = min_moves_to_convert(S, T)
        if result == -1:
            print(f"Case {case}: -1")
        else:
            print(f"Case {case}: {result}")

if __name__ == "__main__":
    main()