def calculate_efficacy(vaccinated, control):
    infected_count = {'A': 0, 'B': 0, 'C': 0}
    vaccinated_count = {'A': 0, 'B': 0, 'C': 0}
    
    for participant in vaccinated:
        if participant[0] == 'Y':
            for i in range(1, 4):
                if participant[i] == 'Y':
                    vaccinated_count[chr(65 + i - 1)] += 1
    
    for participant in control:
        for i in range(1, 4):
            if participant[i] == 'Y':
                infected_count[chr(65 + i - 1)] += 1
    
    efficacy = {}
    for strain in 'ABC':
        if vaccinated_count[strain] == 0:
            efficacy[strain] = 100.0
        else:
            reduction_rate = (infected_count[strain] / sum(infected_count.values())) * 100
            original_rate = (vaccinated_count[strain] / sum(vaccinated_count.values())) * 100
            efficacy[strain] = ((original_rate - reduction_rate) / original_rate) * 100
            if efficacy[strain] < 0:
                efficacy[strain] = 0.0
    
    return [efficacy[strain] if efficacy[strain] > 0 else 'Not Effective' for strain in 'ABC']

# Read input
N = int(input())
vaccinated_group = [input().strip() for _ in range(N)]
control_group = [input().strip() for _ in range(N)]

# Calculate and output efficacy
efficacy_results = calculate_efficacy(vaccinated_group, control_group)
for result in efficacy_results:
    print("{:.6f}".format(result) if isinstance(result, float) else result)