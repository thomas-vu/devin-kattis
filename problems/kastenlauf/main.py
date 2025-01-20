def can_reach(home, bergkirchweih, stores):
    total_beer = 20
    for store in stores:
        distance = abs(home[0] - store[0]) + abs(home[1] - store[1])
        if distance <= total_beer * 50:
            total_beer -= (distance / 50)
        else:
            return "sad"
    final_distance = abs(home[0] - bergkirchweih[0]) + abs(home[1] - bergkirchweih[1])
    if final_distance <= total_beer * 50:
        return "happy"
    else:
        return "sad"

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        home = list(map(int, input().split()))
        stores = [list(map(int, input().split())) for _ in range(n)]
        bergkirchweih = list(map(int, input().split()))
        result = can_reach(home, bergkirchweih, stores)
        print(result)

main()