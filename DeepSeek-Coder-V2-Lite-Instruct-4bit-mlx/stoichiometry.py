def parse_molecule(line):
    molecule = {}
    i = 0
    while i < len(line):
        if line[i].isupper():
            element = line[i]
            i += 1
            while i < len(line) and line[i].islower():
                element += line[i]
                i += 1
            count = 0
            while i < len(line) and line[i].isdigit():
                count = count * 10 + int(line[i])
                i += 1
            if count == 0:
                count = 1
            molecule[element] = count
        elif line[i] == '(': or line[i] == ')':
            i += 1
        else:
            raise ValueError("Invalid character in molecule string")
    return molecule

def balance_equation(lines):
    elements = {}
    coefficients = {}
    for line in lines:
        sign, num_elements = map(int, line[0].split())
        elements_list = parse_molecule(line[1:])
        for element, count in elements_list.items():
            if element not in elements:
                elements[element] = 0
            elements[element] += count * sign
        if line[0][0] == '+':
            coefficients['reactants'] += num_elements
        else:
            coefficients['products'] += num_elements
    
    # Find the least common multiple of all elements
    min_coeff = 1
    for element, count in elements.items():
        if count != 0:
            min_coeff = lcm(min_coeff, abs(count))
    
    # Scale the coefficients to balance the equation
    for element, count in elements.items():
        if count != 0:
            scale_factor = min_coeff / abs(count)
            elements[element] *= scale_factor
    
    return [int(elements['reactants'] / 2), int(min_coeff)]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

# Main function to parse input and output the balanced equation coefficients
def main():
    while True:
        lines = []
        while True:
            line = input().strip()
            if line == '0 0':
                break
            lines.append(line)
        if not lines:
            break
        result = balance_equation(lines)
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()