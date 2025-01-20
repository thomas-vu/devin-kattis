def should_route_to_directory(number):
    str_num = str(number)
    return 1 if str_num[:3] == '555' else 0

# Sample Inputs
inputs = [5551212, 55198760, 505555550, 55500001]

# Outputs
for number in inputs:
    print(should_route_to_directory(number))