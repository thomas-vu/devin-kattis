# Function to determine the number of legs for each creature based on responses from the sphinx
def solve_riddle():
    # Initialize the number of legs for each creature to -1 (unknown)
    axex_legs = -1
    basilisk_legs = -1
    centaur_legs = -1
    
    # Helper function to ask the sphinx a question and return the response
    def ask_sphinx(a, b, c):
        print(f"{a} {b} {c}")
        return int(input())
    
    # Ask the sphinx questions and use responses to deduce the number of legs for each creature
    total_legs = ask_sphinx(1, 1, 1) # Sum of legs for 1 axex, 1 basilisk, and 1 centaur
    sum_legs = ask_sphinx(0, 0, 0) # Sum of legs for no creatures
    sum_legs = ask_sphinx(1, 0, 0) # Sum of legs for 1 axex and no basilisks or centaurs
    sum_legs = ask_sphinx(0, 1, 0) # Sum of legs for 1 basilisk and no axexes or centaurs
    sum_legs = ask_sphinx(0, 0, 1) # Sum of legs for 1 centaur and no axexes or basilisks
    sum_legs = ask_sphinx(1, 1, 0) # Sum of legs for 1 axex and 1 basilisk
    sum_legs = ask_sphinx(1, 0, 1) # Sum of legs for 1 axex and 1 centaur
    sum_legs = ask_sphinx(0, 1, 1) # Sum of legs for 1 basilisk and 1 centaur
    sum_legs = ask_sphinx(2, 0, 0) # Sum of legs for 2 axexes
    sum_legs = ask_sphinx(0, 2, 0) # Sum of legs for 2 basilisks
    sum_legs = ask_sphinx(0, 0, 2) # Sum of legs for 2 centaurs
    
    # Use the responses to deduce the number of legs for each creature
    if total_legs == sum_legs:
        axex_legs = 4
        basilisk_legs = 4
        centaur_legs = 4
    else:
        # If the sum of legs for no creatures matches, it means there are no legs (0)
        if sum_legs == 0:
            axex_legs = 0
            basilisk_legs = 0
            centaur_legs = 0
        else:
            # Use the difference to find out the number of legs for each creature
            diff = total_legs - sum_legs
            if diff == 4:
                centaur_legs = 3
            elif diff == 2:
                basilisk_legs = 4 - sum_legs + centaur_legs
            elif diff == 6:
                axex_legs = 4 - sum_legs + basilisk_legs
            else:
                # If the difference doesn't match any known pattern, it means our initial assumption was wrong
                # We need to re-evaluate the number of legs for each creature based on all responses
                axex_legs = 4 - sum_legs + basilisk_legs + centaur_legs
    
    # Output the number of legs for each creature
    print(f"{axex_legs} {basilisk_legs} {centaur_legs}")

# Run the function to solve the riddle
solve_riddle()