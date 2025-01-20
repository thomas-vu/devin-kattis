import sys

# Read the length of the passcode from the judge
n = int(input())

# Initialize the guess string with empty characters
guess = ''

# Make guesses according to the rules provided by the judge
for _ in range(n):
    # Make a guess and flush the output buffer
    print(guess, end='')
    sys.stdout.flush()
    
    # Read the response from the judge
    response = int(input())
    
    # Update the guess based on the response
    if response == 1:
        guess += 'P'
    elif response == 0:
        break

# If the guess is equal to the passcode, the judge will respond with 2
if len(guess) < n:
    guess += 'A'
    print(guess, flush=True)
else:
    # If the guess is equal to the passcode, terminate the program
    sys.exit()