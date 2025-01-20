from datetime import datetime, timedelta

# Helper function to parse time and day
def parse_time(timestamp):
    return datetime.strptime(timestamp, "%H:%M")

# Helper function to find the next flash time for a star
def next_flash(start, interval):
    now = start
    while now < datetime.now():
        now += timedelta(minutes=interval)
    return now

# Read input timestamps
flash1_time = parse_time(input())
flash2_time = parse_time(input())
interval1 = int(input().replace(":", ""))
interval2 = int(input().replace(":", ""))

# Calculate next flash times for both stars
next_flash1 = next_flash(flash1_time, interval1)
next_flash2 = next_flash(flash2_time, interval2)

# Check for the first same-minute flash
while next_flash1.day == flash1_time.day and next_flash2.day == flash2_time.day:
    if next_flash1.minute == next_flash2.minute:
        day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        print(day[next_flash1.weekday()])
        print(f"{next_flash1.strftime('%H:%M')}")
        break
    next_flash1 = next_flash(next_flash1, interval1)
    next_flash2 = next_flash(next_flash2, interval2)
else:
    print("Never")