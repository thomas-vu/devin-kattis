def optimal_partition(cans):
    total_calories = sum(cans)
    if total_calories % 2 == 0:
        target = total_calories // 2
    else:
        target = (total_calories + 1) // 2
    
    current_sum = 0
    for can in cans:
        current_sum += can
        if current_sum == target:
            return (target, total_calories - target)
        elif current_sum > target:
            return (current_sum, total_calories - current_sum)
    
    # If we reach here, it means the total calories are odd and cannot be perfectly partitioned
    return (total_calories, 0)

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        cans = list(map(int, input().split()))
        first_meal, second_meal = optimal_partition(cans)
        print(f"{first_meal} {second_meal}")

if __name__ == "__main__":
    main()