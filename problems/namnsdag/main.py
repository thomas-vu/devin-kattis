def min_days_to_name_day(friend_name, name_days):
    def count_diff(s1, s2):
        return sum(c1 != c2 for c1, c2 in zip(s1, s2))
    
    min_diff = float('inf')
    target_name = name_days[0]
    
    for name in name_days:
        if friend_name != name and len(friend_name) == len(name):
            diff = count_diff(friend_name, name)
            if diff == 1:
                return 1
            min_diff = min(min_diff, diff)
    
    if min_diff == float('inf'):
        return len(friend_name) + 1
    else:
        return min_diff

# Main function to read input and output the result
def main():
    friend_name = input().strip()
    N = int(input().strip())
    name_days = [input().strip() for _ in range(N)]
    
    result = min_days_to_name_day(friend_name, name_days)
    print(result)

if __name__ == "__main__":
    main()