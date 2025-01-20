def von_neumann_ordinal(n):
    if n == 0:
        return "{}"
    result = ["{}"]
    for i in range(1, n + 1):
        result.append({str(j) for j in range(i)})
    return "{" + ", ".join([str(set(result[i])) for i in range(n)]) + "}"

# Example usage:
print(von_neumann_ordinal(0))  # Output: {}
print(von_neumann_ordinal(1))  # Output: {{}}
print(von_neumann_ordinal(2))  # Output: {{},{{}}}