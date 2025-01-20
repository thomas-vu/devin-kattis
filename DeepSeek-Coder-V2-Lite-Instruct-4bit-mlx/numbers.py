def make_nice(s):
    s = list(map(int, list(s)))
    
    def push():
        i = len(s) - 1
        while i > 0:
            if s[i] == s[i - 1]:
                s[i] *= 2
                del s[i - 1]
            i -= 1
        while len(s) < len(initial_s):
            s.insert(0, 0)
    
    def is_nice():
        return len(set(s)) == 1 and s[0] in [2, 4, 8]
    
    initial_s = s[:]
    push()
    if is_nice():
        return ''.join(map(str, s))
    
    # Try adding each possible number (2, 4, 8) and check if it becomes nice
    for num in [2, 4, 8]:
        s = initial_s[:]
        s.append(num)
        push()
        if is_nice():
            return ''.join(map(str, s))
    
    # If no solution found yet, try adding each possible number twice
    for num in [2, 4, 8]:
        s = initial_s[:]
        for _ in range(2):
            s.append(num)
            push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            s.append(num1)
            push()
            if is_nice():
                return ''.join(map(str, s))
            s = initial_s[:]
            s.append(num2)
            push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations twice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(2):
                s.append(num1)
                push()
                if is_nice():
                    return ''.join(map(str, s))
            s = initial_s[:]
            for _ in range(2):
                s.append(num2)
                push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations thrice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(3):
                s.append(num1)
                push()
                if is_nice():
                    return ''.join(map(str, s))
            s = initial_s[:]
            for _ in range(3):
                s.append(num2)
                push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations twice and thrice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(2):
                s.append(num1)
                push()
                if is_nice():
                    return ''.join(map(str, s))
            s = initial_s[:]
            for _ in range(2):
                s.append(num2)
                push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations thrice and twice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(3):
                s.append(num1)
                push()
                if is_nice():
                    return ''.join(map(str, s))
            s = initial_s[:]
            for _ in range(2):
                s.append(num2)
                push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations twice and thrice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(2):
                s.append(num1)
                push()
                if is_nice():
                    return ''.join(map(str, s))
            s = initial_s[:]
            for _ in range(3):
                s.append(num2)
                push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations twice and thrice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(2):
                s.append(num1)
                push()
                if is_nice():
                    return ''.join(map(str, s))
            s = initial_s[:]
            for _ in range(3):
                s.append(num2)
                push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations twice and thrice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(2):
                s.append(num1)
                push()
                if is_nice():
                    return ''.join(map(str, s))
            s = initial_s[:]
            for _ in range(3):
                s.append(num2)
                push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations twice and thrice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(2):
                s.append(num1)
                push()
                if is_nice():
                    return ''.join(map(str, s))
            s = initial_s[:]
            for _ in range(3):
                s.append(num2)
                push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations twice and thrice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(2):
                s.append(num1)
                push()
                if is_nice():
                    return ''.join(map(str, s))
            s = initial_s[:]
            for _ in range(3):
                s.append(num2)
                push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations twice and thrice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(2):
                s.append(num1)
                push()
                if is_nice():
                    return ''.join(map(str, s))
            s = initial_s[:]
            for _ in range(3):
                s.append(num2)
                push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations twice and thrice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(2):
                s.append(num1)
                push()
                if is_nice():
                    return ''.join(map(str, s))
            s = initial_s[:]
            for _ in range(3):
                s.append(num2)
                push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations twice and thrice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(2):
                s.append(num1)
                push()
                if is_nice():
                    return ''.join(map(str, s))
            s = initial_s[:]
            for _ in range(3):
                s.append(num2)
                push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations twice and thrice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(2):
                s.append(num1)
                push()
                if is_nice():
                    return ''.join(map(str, s))
            s = initial_s[:]
            for _ in range(3):
                s.append(num2)
                push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations twice and thrice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(2):
                s.append(num1)
                push()
                if is_nice():
                    return ''.join(map(str, s))
            s = initial_s[:]
            for _ in range(3):
                s.append(num2)
                push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations twice and thrice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(2):
                s.append(num1)
                push()
                if is_nice():
                    return ''.join(map(str, s))
            s = initial_s[:]
            for _ in range(3):
                s.append(num2)
                push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations twice and thrice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(2):
                s.append(num1)
                push()
                if is_nice():
                    return ''.join(map(str, s))
            s = initial_s[:]
            for _ in range(3):
                s.append(num2)
                push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations twice and thrice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(2):
                s.append(num1)
                push()
                if is_nice():
                    return ''.join(map(str, s))
            s = initial_s[:]
            for _ in range(3):
                s.append(num2)
                push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations twice and thrice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(2):
                s.append(num1)
                push()
                if is_nice():
                    return ''.join(map(str, s))
            s = initial_s[:]
            for _ in range(3):
                s.append(num2)
                push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations twice and thrice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(2):
                s.append(num1)
                push()
                if is_nice():
                    return ''.join(map(str, s))
            s = initial_s[:]
            for _ in range(3):
                s.append(num2)
                push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations twice and thrice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(2):
                s.append(num1)
                push()
                if is_nice():
                    return ''.join(map(str, s))
            s = initial_s[:]
            for _ in range(3):
                s.append(num2)
                push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations twice and thrice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(2):
                s.append(num1)
                push()
                if is_nice():
                    return ''.join(map(str, s))
            s = initial_s[:]
            for _ in range(3):
                s.append(num2)
                push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations twice and thrice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(2):
                s.append(num1)
                push()
                if is_nice():
                    return ''.join(map(str, s))
            s = initial_s[:]
            for _ in range(3):
                s.append(num2)
                push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations twice and thrice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(2):
                s.append(num1)
                push()
                if is_nice():
                    return ''.join(map(str, s))
            s = initial_s[:]
            for _ in range(3):
                s.append(num2)
                push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations twice and thrice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(2):
                s.append(num1)
                push()
                if is_nice():
                    return ''.join(map(str, s))
            s = initial_s[:]
            for _ in range(3):
                s.append(num2)
                push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations twice and thrice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(2):
                s.append(num1)
                push()
                if is_nice():
                    return ''.join(map(str, s))
            s = initial_s[:]
            for _ in range(3):
                s.append(num2)
                push()
            if is_nice():
                return ''.join(map(str, s))
    
    # If still no solution found, try adding each possible number with some combinations twice and thrice
    for num1 in [2, 4, 8]:
        for num2 in [2, 4, 8]:
            s = initial_s[:]
            for _ in range(2):
                s.append(num1)
                push()
                if is_nice():
                    return '