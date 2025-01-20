def count_farms(C, N, farms):
    farm_counts = [0] * 51
    for farm in farms:
        if farm <= C:
            farm_counts[0] += 1
        else:
            count = farm
            day = 0
            while count > C:
                left = (count + 1) // 2
                right = count // 2
                farm_counts[day] += left
                count = right
                day += 1
            if count > 0:
                farm_counts[day] += count
    return farm_counts

def main():
    C, N, M = map(int, input().split())
    farms = [int(input()) for _ in range(N)]
    visit_days = [int(input()) for _ in range(M)]
    
    farm_counts = count_farms(C, N, farms)
    
    for day in visit_days:
        print(farm_counts[day])

if __name__ == "__main__":
    main()