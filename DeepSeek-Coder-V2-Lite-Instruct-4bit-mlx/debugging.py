def find_crashing_line(n, r, p):
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        # Time to run the program up to the midpoint
        time_to_mid = mid * r
        # Time to add printf statements up to the midpoint
        time_to_add_printf = mid * p
        # Total estimated time to find the crashing line in the first half
        total_time_first_half = time_to_mid + time_to_add_printf
        # Time to run the program up to the next midpoint (if necessary)
        time_to_next_mid = (right + 1) * r
        # Time to add printf statements up to the next midpoint (if necessary)
        time_to_add_printf_next = right * p
        # Total estimated time to find the crashing line in the second half
        total_time_second_half = time_to_next_mid + time_to_add_printf_next
        # Choose the strategy that minimizes the worst-case time
        if total_time_first_half < total_time_second_half:
            right = mid
        else:
            left = mid + 1
    # The crashing line is found at the position where left equals right
    return left * r + left * p

# Read input
n, r, p = map(int, input().split())
# Output the worst-case time to find the crashing line
print(find_crashing_line(n, r, p))