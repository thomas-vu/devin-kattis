B, Br, Bs, A, As = map(int, input().split())

# Calculate the total savings for Bob and Alice
Bob_savings = (Br - B) * Bs
Alice_savings = 0
age = A
while Alice_savings <= Bob_savings:
    Alice_savings += As
    age += 1

print(age)