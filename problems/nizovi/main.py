def pretty_print(s):
    def parse_array(arr, indent=0):
        result = []
        for item in arr:
            if isinstance(item, list):
                result.append(' ' * indent + '{')
                result.extend(parse_array(item, indent + 2))
                result.append(' ' * indent + '}')
            else:
                if isinstance(item, str):
                    lines = item.split(',')
                    for line in lines:
                        result.append(' ' * indent + line)
                else:
                    raise ValueError("Invalid item in array")
        return result
    
    arr = eval('[' + s.replace('{', '[').replace('}', ']') + ']')
    return '\n'.join(parse_array(arr))

# Test cases
print(pretty_print("{abc,ono,sto}"))
print(pretty_print("{}"))
print(pretty_print("{znakovi}"))
print(pretty_print("{a,b,{c,d},e,{}}"))