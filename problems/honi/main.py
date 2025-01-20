MOD = 1_000_000_007

def main():
    N = int(input())
    tasks = list(map(int, input().split()))
    difficulties = list(map(int, input().split()))
    
    # Calculate the number of ways to choose tasks for each difficulty
    ways = 1
    for i in range(N):
        if difficulties[i] == 0:
            # If there are no tasks with exactly this difficulty, we can't choose it
            continue
        elif difficulties[i] == 1:
            # If there is exactly one task with this difficulty, we must choose it
            ways *= tasks[i]
            ways %= MOD
        else:
            # If there are multiple tasks with this difficulty, we can choose any of them
            ways *= difficulties[i]
            ways %= MOD
    
    print(ways)

if __name__ == "__main__":
    main()