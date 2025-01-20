def gould_to_ieee(gould):
    sign = (gould[0] >> 7) & 1
    exponent = ((gould[0] & 63) << 4 | (gould[1] >> 4)) - 80
    mantissa = ((gould[1] & 15) << 16 | gould[2] << 8 | gould[3])

    if exponent == 127:
        return '0' * 8
    elif exponent == -96:
        if mantissa == 0:
            return '0' * 8 if sign else '3FF00000'
        elif mantissa & (1 << 23) == 0:
            return '7FF80000' if sign else 'FFF80000'
    elif exponent == -95:
        return '7FF00000' if sign else 'FFF00000'
    elif exponent == -80:
        return (str(bin((1 << 23) | mantissa))[2:].zfill(32)[:8] + '0' * 16) if sign == 0 else ('FFF' + str(bin((1 << 23) | mantissa))[2:].zfill(32)[:8] + '0' * 16)
    else:
        return (str(bin((1 << 23) | mantissa))[2:].zfill(32)[:8] + '0' * 16) if sign == 0 else ('FFF' + str(bin((1 << 23) | mantissa))[2:].zfill(32)[:8] + '0' * 16)

P = int(input())
for _ in range(P):
    K, hex_value = input().split()
    gould = [int(hex_value[i:i+2], 16) for i in range(0, len(hex_value), 2)]
    ieee = gould_to_ieee(gould)
    print(f"{K} {ieee}")