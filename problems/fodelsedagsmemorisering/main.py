def main():
    N = int(input())
    friends = []
    for _ in range(N):
        name, _, birthday = input().split()
        day, month = map(int, birthday.split('/'))
        friends.append((name, int(day), int(month)))
    
    # Sort by birthday and then by Krarkl's preference (name)
    friends.sort(key=lambda x: (x[1], x[2], x[0]))
    
    # Find the friend Krarkl likes the most with a unique birthday
    remembered_friends = []
    i = 0
    while i < N:
        j = i
        unique_birthday = friends[i][1:]
        while j < N and friends[j][1:] == unique_birthday:
            if friends[j][2] > friends[i][2]:  # Compare by Krarkl's preference
                remembered_friends.append(friends[i])
                break
            j += 1
        i = j
    
    # Output the result
    print(len(remembered_friends))
    for friend in sorted([f[0] for f in remembered_friends]):
        print(friend)

if __name__ == "__main__":
    main()