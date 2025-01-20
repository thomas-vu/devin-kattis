import sys
from math import gcd

def is_magic(bitstring):
    p = len(bitstring) + 1
    for m in range(1, p):
        submatrix = [bitstring[i - 1] for i in range(m, len(bitstring) + m, m)]
        if submatrix.count('1') != submatrix.count('0'):
            return False
    return True

def find_magic(p):
    bitstring = '0' * (p - 1)
    for i in range(2 ** (p - 1)):
        bitstring = bin(i)[2:].zfill(p - 1)
        if is_magic(bitstring):
            return bitstring
    return "Impossible"

def main():
    while True:
        p = int(sys.stdin.readline().strip())
        if p == 0:
            break
        result = find_magic(p)
        print(result if result != "Impossible" else "Impossible")

if __name__ == "__main__":
    main()