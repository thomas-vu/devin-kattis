import sys

# Read the maximum number of bottles Maj could consume per day
R = int(input())

# Initialize the variables to keep track of the number of bottles consumed so far and the current day
total_bottles = 0
day = 1
max_day = 85

# Loop through each day until the end of Christmas Eve
while day <= max_day:
    # Ask how many bottles Maj has consumed so far
    print(total_bottles, flush=True)
    
    # Read Maj's response
    response = input()
    
    if response == "exact":
        break  # Exit the loop if Maj has consumed the exact number of bottles
    elif response == "more":
        # If the response is more, we need to find the exact number of bottles consumed so far
        low = total_bottles + 1
        high = min(total_bottles + R, max_day * (R - 1))
        while low < high:
            mid = (low + high) // 2
            print(mid, flush=True)
            response = input()
            if response == "exact":
                break
            elif response == "more":
                low = mid + 1
            else:  # response == "less"
                high = mid - 1
        total_bottles = low if response == "more" else high
    elif response == "less":
        # If the response is less, we need to find the exact number of bottles consumed so far
        high = total_bottles - 1
        while low < high:
            mid = (low + high) // 2
            print(mid, flush=True)
            response = input()
            if response == "exact":
                break
            elif response == "less":
                low = mid + 1
            else:  # response == "more"
                high = mid - 1
        total_bottles = low if response == "less" else high
    day += 1