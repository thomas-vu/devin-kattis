def fits_square_in_circle(L, R):
    # The diagonal of the square must fit within the circle's diameter
    return 2 * (L / 2) <= R

# Main function to take input and output the result
def main():
    L, R = map(int, input().split())
    if fits_square_in_circle(L, R):
        print("fits")
    else:
        print("nope")

# Call the main function
main()