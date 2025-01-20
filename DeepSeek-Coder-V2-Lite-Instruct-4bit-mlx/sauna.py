def find_lowest_and_count(preferences):
    min_temp = float('inf')
    count = 0
    for temp in range(min([pref[0] for pref in preferences]), max([pref[1] for pref in preferences]) + 1):
        if all(a <= temp <= b for a, b in preferences):
            min_temp = min(min_temp, temp)
            count += 1
    return (count, min_temp) if count > 0 else "bad news"

def main():
    N = int(input())
    preferences = [tuple(map(int, input().split())) for _ in range(N)]
    result = find_lowest_and_count(preferences)
    if result == "bad news":
        print("bad news")
    else:
        print(result[0], result[1])

if __name__ == "__main__":
    main()