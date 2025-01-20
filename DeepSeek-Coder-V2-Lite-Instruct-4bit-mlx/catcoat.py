import itertools
from math import comb

# Helper function to parse the color of a cat
def parse_color(color):
    black = red = dilution = '-'
    if 'B' in color:
        black = 'B' if 'B' in color else 'b'
    if 'O' in color:
        red = 'O' if 'O' in color else 'o'
    if 'D' in color:
        dilution = 'D' if 'D' in color else 'd'
    return black, red, dilution

# Helper function to generate all possible genotypes for a cat
def generate_genotypes(black, red, dilution):
    black_genotypes = ['BB', 'Bb', 'bb'] if black != '-' else ['BB', 'Bb', 'bb', 'bB']
    red_genotypes = ['OO', 'Oo'] if red != '-' else ['OO', 'Oo', 'oo']
    dilution_genotypes = ['DD', 'Dd', 'dd'] if dilution != '-' else ['DD', 'Dd', 'dd', 'dD']
    genotypes = list(itertools.product(black_genotypes, red_genotypes, dilution_genotypes))
    return genotypes

# Helper function to calculate the probability of a genotype combination
def calc_probability(genotype1, genotype2):
    prob = 0.5 if genotype2[1] == 'Oo' else 1
    return prob / len(genotype1) if genotype2[0] == 'BB' else prob

# Helper function to calculate the probabilities of offspring colors
def calc_offspring_colors(female, male):
    female_black, female_red, female_dilution = parse_color(female)
    male_black, male_red, male_dilution = parse_color(male)
    
    female_genotypes = generate_genotypes(female_black, female_red, female_dilution)
    male_genotypes = generate_genotypes(male_black, male_red, male_dilution)
    
    probabilities = {}
    for genotype1 in female_genotypes:
        for genotype2 in male_genotypes:
            prob = calc_probability(genotype1, genotype2)
            if genotype2[1] == 'Oo':
                prob *= 0.5
            color = calc_color(genotype1, genotype2)
            if color not in probabilities:
                probabilities[color] = 0
            probabilities[color] += prob
    
    return probabilities

# Helper function to calculate the color of offspring based on genotypes
def calc_color(genotype1, genotype2):
    black = red = dilution = '-'
    if genotype1[0] == 'BB' or genotype2[0] == 'BB':
        black = 'B' if genotype1[0] == 'BB' or genotype2[0] == 'BB' else 'b'
    if genotype1[1] == 'OO' or genotype2[1] == 'OO':
        red = 'O' if genotype1[1] == 'OO' or genotype2[1] == 'OO' else 'o'
    if genotype1[2] == 'DD' or genotype2[2] == 'DD':
        dilution = 'D' if genotype1[2] == 'DD' or genotype2[2] == 'DD' else 'd'
    return f"{black}{red}{dilution}"

# Main function to calculate the most likely color of offspring
def main():
    female = input().strip()
    male = input().strip()
    
    probabilities = calc_offspring_colors(female, male)
    sorted_probabilities = sorted(probabilities.items(), key=lambda x: (-x[1], x[0]))
    
    for color, prob in sorted_probabilities:
        print(f"{color} {prob:.9f}")

if __name__ == "__main__":
    main()