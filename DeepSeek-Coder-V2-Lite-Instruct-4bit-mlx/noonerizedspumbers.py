def swap_prefix(x, y, z):
    def proper_prefixes(num):
        pre = []
        for i in range(1, len(str(num))):
            pre.append(int(str(num)[:i]))
        return pre
    
    x_pre = proper_prefixes(x)
    y_pre = proper_prefixes(y)
    z_pre = proper_prefixes(z)
    
    for x_p in x_pre:
        for y_p in y_pre:
            if str(x_p) + str(y_p) == str(z):
                return f"{x_p} + {y} = {z}"
            elif str(y_p) + str(x_p) == str(z):
                return f"{y} + {x_p} = {z}"
            for z_p in z_pre:
                if str(x_p) + str(y_p) == str(z_p):
                    return f"{x} + {y_p} = {z_p}"
                elif str(y_p) + str(x_p) == str(z_p):
                    return f"{y} + {x_p} = {z_p}"
    
    for x_p in x_pre:
        for z_p in z_pre:
            if str(x_p) + str(z_p) == str(y):
                return f"{x} + {z_p} = {y}"
            elif str(z_p) + str(x_p) == str(y):
                return f"{z_p} + {x} = {y}"
    
    for y_p in y_pre:
        for z_p in z_pre:
            if str(y_p) + str(z_p) == str(x):
                return f"{y} + {z_p} = {x}"
            elif str(z_p) + str(y_p) == str(x):
                return f"{z_p} + {y} = {x}"
    
    return ""

# Read input
line = input().strip()

# Extract numbers and operator
parts = line.split()
x, op, y, _, z = int(parts[0]), parts[1], int(parts[2]), parts[3], int(parts[4])

# Determine the correct equation by swapping prefixes
if op == "+":
    result = swap_prefix(x, y, z)
elif op == "*":
    result = swap_prefix(x, y, z)
else:
    result = ""

# Output the correct equation
print(result)