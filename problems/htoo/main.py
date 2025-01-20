import re
from collections import Counter

def parse_molecule(formula):
    count = {}
    stack = []
    i = 0
    while i < len(formula):
        if formula[i].isupper():
            atom = formula[i]
            i += 1
            num_str = ''
            while i < len(formula) and formula[i].islower():
                num_str += formula[i]
                i += 1
            if num_str:
                number = int(num_str)
            else:
                number = 1
            if stack:
                top = stack[-1]
                if isinstance(top, dict):
                    if atom in top:
                        top[atom] += number
                    else:
                        top[atom] = number
                elif isinstance(top, list):
                    for d in top:
                        if atom in d:
                            d[atom] += number
                        else:
                            d[atom] = number
            else:
                count[atom] = number
        elif formula[i].isdigit():
            num_str = ''
            while i < len(formula) and formula[i].isdigit():
                num_str += formula[i]
                i += 1
            number = int(num_str)
            top = stack[-1]
            if isinstance(top, list):
                for d in top:
                    for key in d:
                        d[key] *= number
            else:
                top *= number
        elif formula[i] == '(': or formula[i] == ')':
            if formula[i] == '(':
                stack.append({})
            else:
                top = stack.pop()
                if stack:
                    inner_top = stack[-1]
                    if isinstance(inner_top, list):
                        inner_top.append(top)
                    else:
                        if isinstance(inner_top, dict):
                            for key in top:
                                if key in inner_top:
                                    inner_top[key] += top[key]
                                else:
                                    inner_top[key] = top[key]
                else:
                    count.update(top)
            i += 1
        else:
            i += 1
    return count

def maximum_output(input_molecule, k):
    input_count = parse_molecule(input_molecule)
    desired_count = parse_molecule(desired_output_molecule)
    
    min_possible = float('inf')
    for atom in desired_count:
        if atom in input_count:
            min_possible = min(min_possible, input_count[atom] // desired_count[atom])
        else:
            min_possible = 0
            break
    
    return min_possible * k

# Sample Inputs and Outputs
input_molecule = "C6H14"
k = 10
desired_output_molecule = "C5H10"
print(maximum_output(input_molecule, k))  # Output: 12