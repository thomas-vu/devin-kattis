def count_distinct_cities(n, cities):
    return len(set(cities))

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        cities = [input().strip() for _ in range(n)]
        print(count_distinct_cities(n, cities))

if __name__ == "__main__":
    main()