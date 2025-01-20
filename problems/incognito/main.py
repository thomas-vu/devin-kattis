def count_disguises(attributes):
    from itertools import combinations
    
    category_to_attributes = {}
    for name, category in attributes:
        if category not in category_to_attributes:
            category_to_attributes[category] = set()
        category_to_attributes[category].add(name)
    
    total_combinations = 1
    for category in category_to_attributes:
        total_combinations *= (len(category_to_attributes[category]) + 1)
    
    return total_combinations - 1

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    num_test_cases = int(data[index])
    index += 1
    results = []
    
    for _ in range(num_test_cases):
        num_attributes = int(data[index])
        index += 1
        attributes = []
        for _ in range(num_attributes):
            name = data[index]
            category = data[index + 1]
            attributes.append((name, category))
            index += 2
        results.append(count_disguises(attributes))
    
    for result in results:
        print(result)

main()