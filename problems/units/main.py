def parse_input():
    while True:
        N = int(input())
        if N == 0:
            break
        units = input().split()
        relations = {}
        for _ in range(N - 1):
            unit1, _, multiplier, unit2 = input().split()
            relations[unit1] = (int(multiplier), unit2)
        
        # Calculate conversion factors from the largest unit to all others
        largest_unit = units[0]
        conversion_factors = {unit: 1 for unit in units}
        
        while relations:
            new_relations = {}
            for unit, (multiplier, dependent_unit) in relations.items():
                conversion_factors[unit] = multiplier * conversion_factors[dependent_unit]
            else:
                relations = new_relations
        
        # Sort units by size in descending order
        sorted_units = sorted(units, key=lambda u: -conversion_factors[u])
        
        # Output the conversion factors
        print(' '.join(f'{conversion_factors[u]}{unit}' for u in sorted_units))

parse_input()