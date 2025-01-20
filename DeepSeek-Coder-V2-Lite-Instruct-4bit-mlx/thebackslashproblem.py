def escape_string(s, n):
    def is_special(c):
        return c in "!#%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    def escape(s):
        return ''.join('\\' + c if is_special(c) else c for c in s)

    result = s
    for _ in range(n):
        result = escape(result)
    return result

while True:
    try:
        n = int(input())
        s = input()
        escaped_string = escape_string(s, n)
        print(escaped_string)
    except EOFError:
        break