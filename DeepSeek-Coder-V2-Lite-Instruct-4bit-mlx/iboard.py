def is_safe_to_leave(s):
    pressed = set()
    for char in s:
        code = ord(char)
        bits = [(code >> i) & 1 for i in range(7)][::-1]
        for bit, state in enumerate(bits):
            if (bit, state) not in pressed:
                pressed.add((bit, state))
            else:
                pressed.remove((bit, state))
    return "free" if not pressed else "trapped"

while True:
    try:
        s = input()
        print(is_safe_to_leave(s))
    except EOFError:
        break