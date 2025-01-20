def choose_friend(n, friends):
    position = 0
    for _ in range(n):
        words = ["úllen", "dúllen", "doff", "kikke", "lane", "koff", "bikke", "bane"]
        for word in words:
            position = (position + 1) % n
    return friends[position]

n = int(input())
friends = input().split()
chosen_friend = choose_friend(n, friends)
print(chosen_friend)