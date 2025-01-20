def chew_apple(n, problems):
    left = []
    right = []
    
    for i in range(n):
        tooth, condition = problems[i].split()
        if condition == 'b':
            left.append(int(tooth))
        elif condition == 'm':
            right.append(int(tooth))
    
    if not left or not right:
        return 1
    
    left_valid = all(tooth >= 0 for tooth in left)
    right_valid = all(tooth < 0 for tooth in right)
    
    if left_valid and right_valid:
        return 0
    elif not left_valid or not right_valid:
        return 2

# Sample Inputs
input1 = [
    '1',
    '-5 b'
]
print(chew_apple(int(input1[0]), input1[1:]))  # Expected Output: 1

input2 = [
    '9',
    '8- m',
    '7- m',
    '6- m',
    '5- m',
    '4- m',
    '3- m',
    '2- m',
    '1- b',
    '+3 m'
]
print(chew_apple(int(input2[0]), input2[1:]))  # Expected Output: 0

input3 = [
    '9',
    '8- m',
    '7- m',
    '6- m',
    '5- m',
    '4- m',
    '3- m',
    '2- m',
    '1- m',
    '+3 b'
]
print(chew_apple(int(input3[0]), input3[1:]))  # Expected Output: 2

input4 = [
    '15',
    '6+ b',
    '+2 m',
    '+3 m',
    '+4 m',
    '+5 m',
    '+6 m',
    '+7 m',
    '+8 m',
    '-1 m',
    '-2 m',
    '-3 m',
    '-4 m',
    '-5 m',
    '-6 m',
    '-7 m'
]
print(chew_apple(int(input4[0]), input4[1:]))  # Expected Output: 0