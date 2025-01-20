import math

def calculate_entropy(probabilities):
    entropy = 0.0
    for prob in probabilities:
        if prob > 0:
            entropy -= prob * math.log2(prob)
    return entropy

def main():
    n = int(input())
    probabilities = list(map(float, input().split()))
    
    # Calculate the entropy of each weather type
    total_entropy = calculate_entropy(probabilities)
    
    # Calculate the minimum expected number of bits using Shannon entropy
    min_expected_bits = total_entropy / n
    
    print("{:.10f}".format(min_expected_bits))

if __name__ == "__main__":
    main()