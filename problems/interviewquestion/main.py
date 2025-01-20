def find_fizz_buzz(c, d, transcript):
    for a in range(1, 10**6 + 1):
        for b in range(1, 10**6 + 1):
            valid = True
            for i in range(c, d + 1):
                if (i - c) % a == 0 and (i - c) % b != 0:
                    if transcript[i - c] != "Fizz":
                        valid = False
                        break
                elif (i - c) % b == 0 and (i - c) % a != 0:
                    if transcript[i - c] != "Buzz":
                        valid = False
                        break
                elif (i - c) % a == 0 and (i - c) % b == 0:
                    if transcript[i - c] != "FizzBuzz":
                        valid = False
                        break
                elif i % a != 0 and i % b != 0:
                    if transcript[i - c] != str(i):
                        valid = False
                        break
            if valid:
                return a, b

# Read input
c, d = map(int, input().split())
transcript = list(map(str, input().split()))

# Find and output the solution
a, b = find_fizz_buzz(c, d, transcript)
print(a, b)