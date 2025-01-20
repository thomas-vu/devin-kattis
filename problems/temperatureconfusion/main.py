from fractions import Fraction

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return Fraction((fahrenheit - 32) * 5, 9)

# Read input from stdin
fahrenheit = input()

# Convert the input to a Fraction and handle negative values
fahrenheit = Fraction(fahrenheit) if fahrenheit[0] != '-' else -Fraction(fahrenheit[1:])

# Convert Fahrenheit to Celsius and output the result in lowest terms
celsius = fahrenheit_to_celsius(fahrenheit)
print(celsius.numerator, celsius.denominator, sep='/')