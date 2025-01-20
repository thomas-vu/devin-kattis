def solve():
    while True:
        N = int(input())
        if N == 0:
            break
        mansions = [int(input()) for _ in range(N)]
        total_value = sum(mansions)
        target_value = total_value / 2
        mansions.sort()
        
        left, right = 0, N - 1
        sum_left, sum_right = mansions[left], mansions[right]
        
        while left < right:
            if sum_left == target_value:
                break
            elif sum_left < target_value:
                left += 1
                sum_left += mansions[left]
            else:
                right -= 1
                sum_right += mansions[right]
        
        sold_value = min(sum_left, sum_right)
        print(total_value - sold_value * 2)

solve()