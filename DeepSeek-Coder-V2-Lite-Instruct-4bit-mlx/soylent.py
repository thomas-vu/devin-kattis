def calculate_bottles(calories):
    daily_requirement = 2000
    bottle_calories = 400
    bottles_needed = (daily_requirement + bottle_calories - 1) // bottle_calories
    return bottles_needed

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(calculate_bottles(N))

if __name__ == "__main__":
    main()