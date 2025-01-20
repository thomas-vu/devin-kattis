def calculate_throws(score):
    if score == 0:
        return []
    for i in range(1, 21):
        if score - (3 * i) == 0:
            return ["triple " + str(i)]
    for i in range(1, 21):
        if score - (2 * i) == 0:
            return ["double " + str(i)]
    if score - 25 == 0:
        return ["single bull"]
    if score - 50 == 0:
        return ["bullseye"]
    
    for i in range(1, 21):
        if score - i == 0:
            return ["single " + str(i)]
    
    for i in range(1, 21):
        for j in range(1, 21):
            if score - (3 * i) - j == 0:
                return ["triple " + str(i), "single " + str(j)]
            if score - i - (3 * j) == 0:
                return ["single " + str(i), "triple " + str(j)]
            if score - i - (2 * j) == 0:
                return ["single " + str(i), "double " + str(j)]
            if score - (2 * i) - j == 0:
                return ["double " + str(i), "single " + str(j)]
    
    for i in range(1, 21):
        for j in range(1, 21):
            for k in range(1, 21):
                if score - i - j - k == 0:
                    return ["single " + str(i), "single " + str(j), "single " + str(k)]
                if score - (3 * i) - j - k == 0:
                    return ["triple " + str(i), "single " + str(j), "single " + str(k)]
                if score - i - (3 * j) - k == 0:
                    return ["single " + str(i), "triple " + str(j), "single " + str(k)]
                if score - i - j - (3 * k) == 0:
                    return ["single " + str(i), "single " + str(j), "triple " + str(k)]
                if score - (2 * i) - j - k == 0:
                    return ["double " + str(i), "single " + str(j), "single " + str(k)]
                if score - i - (2 * j) - k == 0:
                    return ["single " + str(i), "double " + str(j), "single " + str(k)]
                if score - i - j - (2 * k) == 0:
                    return ["single " + str(i), "single " + str(j), "double " + str(k)]
    
    return ["impossible"]

def main():
    T = int(input().strip())
    throws = calculate_throws(T)
    if throws == ["impossible"]:
        print("impossible")
    else:
        for throw in throws:
            print(throw)

if __name__ == "__main__":
    main()