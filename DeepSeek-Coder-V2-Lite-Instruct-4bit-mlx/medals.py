def can_canada_win(countries):
    canada = countries[0]
    others = countries[1:]
    
    # Calculate the total number of medals for all countries
    total_medals = sum(country[1] + country[2] + country[3] for country in others)
    
    # Check all possible weight vectors of the form (1/n^j, 1/n^k, 1/n^l)
    for j in range(21):
        for k in range(21):
            for l in range(21):
                # Calculate the score for Canada and each other country with the current weight vector
                canada_score = (canada[1] / total_medals**j, canada[2] / total_medals**k, canada[3] / total_medals**l)
                other_scores = [(country[1] / total_medals**j, country[2] / total_medals**k, country[3] / total_medals**l) for country in others]
                
                # Sort the countries based on their scores
                sorted_countries = sorted(countries, key=lambda x: (-x[1] / total_medals**j, -x[2] / total_medals**k, -x[3] / total_medals**l))
                
                # Check if Canada is ranked first
                canada_rank = 1
                for i, country in enumerate(sorted_countries):
                    if country[0] == canada[0]:
                        break
                    elif country[0] != canada[0]:
                        canada_rank += 1
                
                if canada_rank == 1:
                    return True
    return False

while True:
    c = int(input())
    if c == 0:
        break
    
    countries = []
    for _ in range(c):
        name, g, s, b = input().split()
        countries.append((name, int(g), int(s), int(b)))
    
    if can_canada_win(countries):
        print("Canada wins!")
    else:
        print("Canada cannot win.")