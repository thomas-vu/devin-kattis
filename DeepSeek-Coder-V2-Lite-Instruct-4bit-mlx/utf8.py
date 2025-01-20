def validUTF8(bytes_sequence):
    i = 0
    n = len(bytes_sequence)
    
    while i < n:
        if bytes_sequence[i][0] == '0':
            i += 1
        elif bytes_sequence[i][:3] == '110':
            count = 0
            while i < n and bytes_sequence[i][:2] == '10':
                count += 1
                i += 1
            if count < 1:
                return "invalid"
        elif bytes_sequence[i][:4] == '1110':
            count = 0
            while i < n and bytes_sequence[i][:2] == '10':
                count += 1
                i += 1
            if count < 2:
                return "invalid"
        elif bytes_sequence[i][:5] == '11110':
            count = 0
            while i < n and bytes_sequence[i][:2] == '10':
                count += 1
                i += 1
            if count < 3:
                return "invalid"
        else:
            return "invalid"
    
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    
    for byte in bytes_sequence:
        if len(byte) == 8 and byte[0] == '0':
            count1 += 1
        elif len(byte) == 8 and byte[:3] == '110':
            count2 += 1
        elif len(byte) == 8 and byte[:4] == '1110':
            count3 += 1
        elif len(byte) == 8 and byte[:5] == '11110':
            count4 += 1
        else:
            return "invalid"
    
    return (count1, count2, count3, count4)

# Read input
n = int(input())
bytes_sequence = [input().strip() for _ in range(n)]

# Check validity and count character encodings
result = validUTF8(bytes_sequence)
if result == "invalid":
    print("invalid")
else:
    count1, count2, count3, count4 = result
    print(count1)
    print(count2)
    print(count3)
    print(count4)