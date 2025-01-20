def min_result(a, b, c):
    return min(eval('a+b-c'), eval('a-b+c'), eval('a*b*c'), eval('a*(b+c)'), eval('(a+b)*c'), eval('a*b+c'))

# Test cases
print(min_result(2, 3, 5))  # Output: 0
print(min_result(9, 9, 9))  # Output: 0
print(min_result(5, 7, 3))  # Output: 1