def convert_seconds(s):
    hours = s // 3600
    minutes = (s % 3600) // 60
    seconds = s % 60
    return f"{hours} : {minutes} : {seconds}"

# Sample Input 1
print(convert_seconds(10000))  # Output: 10000 : 16 : 40

# Sample Input 2
print(convert_seconds(80000))  # Output: 80000 : 22 : 13 : 20