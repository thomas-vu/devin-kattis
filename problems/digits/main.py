def find_cycle(x0):
    i = 1
    while True:
        if len(str(x0)) == x0:
            return i
        x0 = len(str(x0))
        i += 1

def main():
    while True:
        x0 = input()
        if x0 == "END":
            break
        print(find_cycle(int(x0)))

if __name__ == "__main__":
    main()