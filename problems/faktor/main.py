def min_bribes(A, I):
    # Calculate the total number of citations needed to achieve the desired impact factor
    min_citations = (I * A)
    
    # Calculate the number of citations per article to achieve the total citations needed
    citations_per_article = (min_citations + A - 1) // A
    
    return citations_per_article * A - min_citations

# Read input
A, I = map(int, input().split())

# Output the result
print(min_bribes(A, I))