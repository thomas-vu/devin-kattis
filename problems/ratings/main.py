def rank_restaurant(ratings):
    total_sum = sum(ratings)
    ratings_list = list(ratings)
    ratings_list.sort()
    
    count = 0
    for rating in ratings_list:
        if rating <= total_sum:
            count += 1
        else:
            break
    return count

def main():
    while True:
        line = input().split()
        n = int(line[0])
        if n == 0:
            break
        ratings = list(map(int, line[1:]))
        result = rank_restaurant(ratings)
        print(result)

if __name__ == "__main__":
    main()