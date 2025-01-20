def calculate_score(sven, friends):
    score = 0
    max_possible_score = 0
    
    for i in range(len(sven)):
        sven_choice = sven[i]
        friend_choices = [friend[i] for friend in friends]
        
        # Calculate actual score
        if sven_choice == 'S':
            if all(friend == 'R' for friend in friend_choices):
                score += 2
            elif any(friend == 'S' for friend in friend_choices):
                score += 1
        
        elif sven_choice == 'P':
            if all(friend == 'S' for friend in friend_choices):
                score += 2
            elif any(friend == 'P' for friend in friend_choices):
                score += 1
        
        elif sven_choice == 'R':
            if all(friend == 'P' for friend in friend_choices):
                score += 2
            elif any(friend == 'R' for friend in friend_choices):
                score += 1
        
        # Calculate max possible score
        if sven_choice == 'S':
            max_possible_score += sum(1 for friend in friend_choices if friend == 'R') * 2
            max_possible_score += sum(1 for friend in friend_choices if friend == 'S')
        
        elif sven_choice == 'P':
            max_possible_score += sum(1 for friend in friend_choices if friend == 'S') * 2
            max_possible_score += sum(1 for friend in friend_choices if friend == 'P')
        
        elif sven_choice == 'R':
            max_possible_score += sum(1 for friend in friend_choices if friend == 'P') * 2
            max_possible_score += sum(1 for friend in friend_choices if friend == 'R')
    
    return score, max_possible_score

# Main function to read input and output the result
def main():
    R = int(input())
    sven_choices = input()
    N = int(input())
    friends_choices = [input() for _ in range(N)]
    
    actual_score, max_possible_score = calculate_score(sven_choices, friends_choices)
    print(actual_score)
    print(max_possible_score)

if __name__ == "__main__":
    main()