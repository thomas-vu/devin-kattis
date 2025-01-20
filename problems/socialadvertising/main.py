def min_ads(friends):
    n = len(friends)
    visited = [False] * n
    
    def dfs(user):
        if visited[user]:
            return 0
        visited[user] = True
        count = 1
        for friend in friends[user]:
            count += dfs(friend)
        return count
    
    min_ads = 0
    for i in range(n):
        if not visited[i]:
            min_ads += dfs(i) - 1
    return min_ads

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        friends_list = []
        for _ in range(n):
            line = list(map(int, input().split()))
            d = line[0]
            friends_list.append(line[1:])
        print(min_ads(friends_list))

if __name__ == "__main__":
    main()