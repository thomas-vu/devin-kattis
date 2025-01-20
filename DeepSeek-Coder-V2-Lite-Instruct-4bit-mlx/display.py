def display_time(time):
    digits = {
        '0': ["+---+", "|   |", "| o |", "|   |", "+---+"],
        '1': ["+   +", "  |  ", "  |  ", "  |  ", "+   +"],
        '2': ["+---+", "    |", "+--+|", "|    ", "+---+"],
        '3': ["+---+", "    |", "+--+|", "    |", "+---+"],
        '4': ["+   +", "| o |", "+--+|", "    |", "+   +"],
        '5': ["+---+", "|    ", "+--+|", "    |", "+---+"],
        '6': ["+---+", "|   |", "+--+|", "| o |", "+---+"],
        '7': ["+---+", "    |", "  + |", "    |", "+   +"],
        '8': ["+---+", "| o |", "+--+|", "| o |", "+---+"],
        '9': ["+---+", "| o |", "+--+|", "    |", "+---+"],
        ':': ["   ", " o ", "   ", " o ", "   "]
    }
    
    def get_digit(d):
        if d.isdigit():
            return digits[d]
        else:
            return digits[':']
    
    h1, h2, _, m1, m2 = time
    d1, d2, d3, d4, d5, d6 = get_digit(h1), get_digit(h2), digits[':'][0], get_digit(m1), get_digit(m2)
    
    display = [""] * 7
    for i in range(5):
        if i == 0:
            display[i] += d1[0] + "   " + d2[0] + "     "
        elif i == 1:
            display[i] += d3[0] + "   " + d4[0] + "     "
        elif i == 2:
            display[i] += d5[0] + "   " + d6[0] + "  o  "
        elif i == 3:
            display[i] += d1[1] + "   " + d2[1] + "     "
        elif i == 4:
            display[i] += d3[1] + "   " + d4[1] + "     "
        elif i == 5:
            display[i] += d5[1] + "   " + d6[1] + "  o  "
        elif i == 6:
            display[i] += d1[2] + "   " + d2[2] + "     "
        elif i == 7:
            display[i] += d3[2] + "   " + d4[2] + "     "
        elif i == 8:
            display[i] += d5[2] + "   " + d6[2] + "  o  "
        elif i == 9:
            display[i] += d1[3] + "   " + d2[3] + "     "
        elif i == 10:
            display[i] += d3[3] + "   " + d4[3] + "     "
        elif i == 11:
            display[i] += d5[3] + "   " + d6[3] + "  o  "
        elif i == 12:
            display[i] += d1[4] + "   " + d2[4] + "     "
        elif i == 13:
            display[i] += d3[4] + "   " + d4[4] + "     "
        elif i == 14:
            display[i] += d5[4] + "   " + d6[4] + "  o  "
    
    for row in display:
        print(row)
    print()

times = []
while True:
    time = input().strip()
    if time == 'end':
        break
    times.append(time)

for time in times:
    display_time(time)