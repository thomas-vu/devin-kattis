def determine_function_type(domain, codomain, mappings):
    domain_set = set()
    codomain_set = set()
    mapping_dict = {}
    
    for line in mappings:
        x, y = line.split(" -> ")
        domain_set.add(x)
        codomain_set.add(y)
        mapping_dict[x] = y
    
    injective = len(mapping_dict) == len(set(mapping_dict.values()))
    surjective = set(codomain) == set(mapping_dict.values())
    
    if injective and surjective:
        return "bijective"
    elif injective:
        return "injective"
    elif surjective:
        return "surjective"
    else:
        return "neither injective nor surjective"
    
while True:
    try:
        domain_input = input()
        codomain_input = input()
        n = int(input())
        mappings = [input().strip() for _ in range(n)]
        
        print(determine_function_type([word.strip() for word in domain_input[7:].split()], [word.strip() for word in codomain_input[8:].split()], mappings))
    except EOFError:
        break