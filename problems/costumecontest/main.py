def main():
    N = int(input())
    costumes = [input().strip() for _ in range(N)]
    category_count = {}
    
    for costume in costumes:
        category = tuple(costume.split())[0]
        if category in category_count:
            category_count[category] += 1
        else:
            category_count[category] = 1
    
    max_count = max(category_count.values())
    winners = [cat for cat, count in category_count.items() if count == max_count]
    winners.sort()
    
    for winner in winners:
        print(winner)

if __name__ == "__main__":
    main()