def detect_zombie(message):
    if "(:)" in message or ":)" in message:
        return "alive"
    elif ":(" in message or "(:" in message:
        return "undead"
    else:
        return "machine"

# Read input from standard input
import sys
input_line = sys.stdin.readline().strip()
print(detect_zombie(input_line))