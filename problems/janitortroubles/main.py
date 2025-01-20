import math

def max_quadrilateral_area(s1, s2, s3, s4):
    # The maximum quadrilateral area can be found using Brahmagupta's formula for cyclic quadrilaterals
    # which is sqrt((s - a)(s - b)(s - c)(s - d)) where s is the semiperimeter and a, b, c, d are the side lengths
    s = (s1 + s2 + s3 + s4) / 2.0
    area = math.sqrt((s - s1) * (s - s2) * (s - s3) * (s - s4))
    return area

# Read input from stdin
input_line = input().strip()
side_lengths = list(map(int, input_line.split()))

# Calculate and output the maximal area
area = max_quadrilateral_area(*side_lengths)
print("{:.10f}".format(area))