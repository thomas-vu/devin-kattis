def count_errands(n, house, workplace, errands):
    xh, yh = house
    xw, yw = workplace
    errands_set = set(map(tuple, errands))
    
    count = 0
    for x, y in errands_set:
        if (xh <= x <= xw or xh >= x >= xw) and (yh <= y <= yw or yh >= y >= yw):
            count += 1
    return count

# Read input
n = int(input())
x_h, y_h, x_w, y_w = map(int, input().split())
errands = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(count_errands(n, (x_h, y_h), (x_w, y_w), errands))