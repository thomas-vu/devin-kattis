import sys

def ipv4_to_ptr(ip):
    parts = ip.split('.')
    parts.reverse()
    return '.'.join(parts) + '.in-addr.arpa.'

def ipv6_to_ptr(ip):
    parts = ip.split(':')
    hex_parts = []
    for part in parts:
        if part == '':
            hex_parts.extend(['0'] * (8 - len(parts)))
        else:
            hex_parts.append(part)
    hex_str = ''.join([f'{int(x):04x}' for x in hex_parts])
    reversed_hex = hex_str[::-1].replace(':', '.')
    return reversed_hex + '.ip6.arpa.'

def main():
    ip = sys.stdin.readline().strip()
    if all(part in '0123456789' for part in ip.split('.')):
        print(ipv4_to_ptr(ip))
    else:
        print(ipv6_to_ptr(ip))

if __name__ == "__main__":
    main()