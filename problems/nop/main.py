def count_nop(program):
    nop = 0
    i = 0
    while i < len(program):
        if program[i].isupper():
            instr_len = 1 + int(program[i+1:].split('a')[0], 16)
            i += instr_len + 1
        else:
            param_count = len(program[i:].split('a')) - 1
            i += param_count + 1
        nop += 1
    return nop - (len(program) // 4)

# Sample Input 1
print(count_nop("Abcd"))  # Output: 0

# Sample Input 2
print(count_nop("EaEbFabG"))  # Output: 5

# Sample Input 3
print(count_nop("AbcbBccCDefgh"))  # Output: 4